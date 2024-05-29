class LuaFunctionConversionError(Exception):
    def __init__(self, message="Converting lua function to dict not allowed"):
        self.message = message
        super().__init__(self.message)