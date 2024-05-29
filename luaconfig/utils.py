from luaconfig.exceptions import LuaFunctionConversionError

def is_list_table(table):
    return all([type(i) == int for i in table.keys()])

def table_to_list(table):
    if is_list_table(table):
        return list(table.values())

def lua_to_py_function(func):
    def function(*args, **kwargs):
        return func(*args, **kwargs)
    return function

def dict_to_lua_table(d):
    def serialize(value):
        if isinstance(value, str):
            return f'"{value}"'
        elif isinstance(value, (int, float)):
            return str(value)
        elif isinstance(value, list):
            return '{' + ', '.join(serialize(v) for v in value) + '}'
        elif isinstance(value, dict):
            return dict_to_lua_table(value)
        elif callable(value):
            raise LuaFunctionConversionError
        else:
            raise TypeError(f"Unsupported data type: {type(value)}")

    items = [f'["{k}"] = {serialize(v)}' for k, v in d.items()]
    return '{' + ', '.join(items) + '}'

def python_to_lua(data):
    result = ""
    for key, value in data.items():
        if isinstance(value, dict):
            table = dict_to_lua_table(value)
            result += f"{key} = {table}\n"
        elif isinstance(value, str):
            result += f"{key} = \"{value}\"\n"
        elif callable(value):
            raise LuaFunctionConversionError
        else:
            result += f"{key} = {value}\n"
    return result