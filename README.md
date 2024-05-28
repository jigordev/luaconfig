# LuaConfig Library

LuaConfig is a Python library that facilitates reading, modifying, and saving Lua configuration files. It provides methods to convert Lua configurations to Python dictionaries, JSON, and YAML formats.

## Installation

Install LuaConfig using pip:

```bash
pip install luaconfig
```

## Usage

### Initialization

To use LuaConfig, initialize it with the path to your Lua configuration file:

```python
from luaconfig import LuaConfig

config = LuaConfig('path/to/config.lua')
```

### Loading Configuration

The configuration is automatically loaded when the `LuaConfig` object is initialized. 

### Getting Values

Retrieve values from the configuration using the `get_value` method:

```python
value = config.get_value('key', default='default_value')
```

### Setting Values

Set values in the configuration using the `set_value` method:

```python
config.set_value('key', 'new_value')
```

### Saving Configuration

Save the modified configuration back to the file:

```python
config.save()
```

### Converting to Dictionary

Convert the Lua configuration to a Python dictionary:

```python
config_dict = config.to_dict()
```

### Converting to JSON

Convert the Lua configuration to JSON:

```python
config_json = config.to_json()
print(config_json)
```

### Converting to YAML

Convert the Lua configuration to YAML:

```python
config_yaml = config.to_yaml()
print(config_yaml)
```

## Error Handling

LuaConfig provides custom exceptions to handle errors during conversions:

- `LuaFuncToDict`: Raised when attempting to convert a Lua function to a dictionary without allowing functions.
- `LuaFuncToJSON`: Raised when converting to JSON and encountering a Lua function.
- `LuaFuncToYAML`: Raised when converting to YAML and encountering a Lua function.

## Dependencies

LuaConfig depends on the following libraries:

- `lupa`: A Python wrapper for LuaJIT.
- `PyYAML`: A YAML parser and emitter for Python.
- `json`: Included in the Python standard library.

## Example

Here's a complete example demonstrating the use of LuaConfig:

```python
from luaconfig import LuaConfig

# Initialize the LuaConfig with the path to the Lua file
config = LuaConfig('path/to/config.lua')

# Get a value from the configuration
value = config.get_value('some.key', default='default_value')
print(f'Some key value: {value}')

# Set a new value in the configuration
config.set_value('some.key', 'new_value')

# Save the configuration back to the file
config.save()

# Convert the configuration to a Python dictionary
config_dict = config.to_dict()
print(config_dict)

# Convert the configuration to JSON
config_json = config.to_json()
print(config_json)

# Convert the configuration to YAML
config_yaml = config.to_yaml()
print(config_yaml)
```

## License

LuaConfig is licensed under the MIT License. See the LICENSE file for more information.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas.