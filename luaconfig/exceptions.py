class LuaFuncToDict(Exception):
    def __init__(self, message="Converting lua function to dict not allowed"):
        self.message = message
        super().__init__(self.message)

class LuaFuncToJSON(Exception):
    def __init__(self, message="Converting lua function to JSON not allowed"):
        self.message = message
        super().__init__(self.message)

class LuaFuncToYAML(Exception):
    def __init__(self, message="Converting lua function to YAML not allowed"):
        self.message = message
        super().__init__(self.message)