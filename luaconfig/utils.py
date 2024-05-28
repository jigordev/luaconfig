def is_list_table(table):
    return all([type(i) == int for i in table.keys()])

def table_to_list(table):
    if is_list_table(table):
        return list(table.values())

def lua_to_py_function(func):
    def function(*args, **kwargs):
        return func(*args, **kwargs)
    return function