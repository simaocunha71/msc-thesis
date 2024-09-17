
def remove_nested(nested_tup):
    return tuple(filter(lambda x: not isinstance(x, tuple), nested_tup))


