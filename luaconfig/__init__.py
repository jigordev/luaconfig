import json, yaml, lupa
from lupa import LuaRuntime
from luaconfig.utils import is_list_table, table_to_list, lua_to_py_function
from luaconfig.exceptions import LuaFuncToDict, LuaFuncToJSON, LuaFuncToYAML
from luaconfig.consts import DEFAULT_LUA_KEYS

class LuaConfig:
    def __init__(self, filepath):
        self.filepath = filepath
        self.lua = LuaRuntime(unpack_returned_tuples=True)
        self.config = self.load_config()

    def load_config(self):
        config = {}
        with open(self.filepath, 'r', encoding='utf-8') as file:
            lua_code = file.read()
            self.lua.execute(lua_code)
            
            for key, value in self.lua.globals().items():
                type_str = str(type(value))
                if key in DEFAULT_LUA_KEYS:
                    continue
                
                config[key] = value
        return config

    def get_value(self, key, default=None):
        keys = key.split('.')
        value = self.config
        try:
            for k in keys:
                value = value[k]
            return value
        except KeyError:
            return default

    def set_value(self, key, value):
        keys = key.split('.')
        config_section = self.config
        for k in keys[:-1]:
            config_section = config_section.setdefault(k, {})
        config_section[keys[-1]] = value

    def save(self):
        with open(self.filepath, 'w', encoding='utf-8') as file:
            file.write(self.lua.table_to_string(self.config))

    def to_dict(self, allow_function=False):
        def _to_dict_recursive(data):
            result = {}
            for key, value in data.items():
                if lupa.lua_type(value) == "function":
                    if allow_function:
                        result[key] = lua_to_py_function(value)
                    else:
                        raise LuaFuncToDict
                elif lupa.lua_type(value) == "table":
                    table = _to_dict_recursive(value)
                    if is_list_table(table):
                        result[key] = table_to_list(table)
                    else:
                        result[key] = table
                else:
                    result[key] = value
            return result
        result = _to_dict_recursive(self.config)
        return result

    def to_json(self):
        try:
            dict_config = self.to_dict()
        except LuaFuncToDict:
            raise LuaFuncToJSON
        return json.dumps(dict_config)

    def to_yaml(self):
        try:
            dict_config = self.to_dict()
        except LuaFuncToDict:
            raise LuaFuncToYAML
        return yaml.dump(dict_config, default_flow_style=False)