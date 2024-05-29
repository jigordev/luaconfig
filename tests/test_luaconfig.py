import pytest
import json
import yaml
from luaconfig import LuaConfig
from luaconfig.exceptions import LuaFunctionConversionError

lua_content = """
config_value = 'test_value'
nested_table = { key = 'value' }
"""

@pytest.fixture
def lua_file(tmp_path):
    file = tmp_path / "config.lua"
    file.write_text(lua_content)
    return file

def test_load_config(lua_file):
    config = LuaConfig(lua_file)
    assert 'config_value' in config.config
    assert config.config['config_value'] == 'test_value'
    assert 'nested_table' in config.config
    assert config.config['nested_table']['key'] == 'value'

def test_get_value(lua_file):
    config = LuaConfig(lua_file)
    assert config.get_value('config_value') == 'test_value'
    assert config.get_value('nested_table.key') == 'value'
    assert config.get_value('nonexistent_key', default='default_value') == 'default_value'

def test_set_value(lua_file):
    config = LuaConfig(lua_file)
    config.set_value('new_key', 'new_value')
    assert config.get_value('new_key') == 'new_value'
    config.set_value('nested_table.new_key', 'new_nested_value')
    assert config.get_value('nested_table.new_key') == 'new_nested_value'

def test_save(lua_file, tmp_path):
    config = LuaConfig(lua_file)
    new_file = tmp_path / "new_config.lua"
    config.filepath = new_file
    config.set_value('new_key', 'new_value')
    config.save()

    # Carregar a nova configuração e verificar o valor
    new_config = LuaConfig(new_file)
    assert new_config.get_value('new_key') == 'new_value'

def test_to_dict(lua_file):
    config = LuaConfig(lua_file)
    config_dict = config.to_dict()
    assert config_dict['config_value'] == 'test_value'
    assert config_dict['nested_table']['key'] == 'value'

def test_to_json(lua_file):
    config = LuaConfig(lua_file)
    json_str = config.to_json()
    config_dict = json.loads(json_str)
    assert config_dict['config_value'] == 'test_value'
    assert config_dict['nested_table']['key'] == 'value'

def test_to_yaml(lua_file):
    config = LuaConfig(lua_file)
    yaml_str = config.to_yaml()
    config_dict = yaml.safe_load(yaml_str)
    assert config_dict['config_value'] == 'test_value'
    assert config_dict['nested_table']['key'] == 'value'

def test_to_dict_with_function(lua_file):
    config = LuaConfig(lua_file)
    config.set_value('func', config.lua.eval('function() return 1 end'))
    with pytest.raises(LuaFunctionConversionError):
        config.to_dict()

def test_to_json_with_function(lua_file):
    config = LuaConfig(lua_file)
    config.set_value('func', config.lua.eval('function() return 1 end'))
    with pytest.raises(LuaFunctionConversionError):
        config.to_json()

def test_to_yaml_with_function(lua_file):
    config = LuaConfig(lua_file)
    config.set_value('func', config.lua.eval('function() return 1 end'))
    with pytest.raises(LuaFunctionConversionError):
        config.to_yaml()
