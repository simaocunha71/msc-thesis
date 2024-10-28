def remove_nested(tup):
    def inner(x):
        return isinstance(x, tuple)
    return tuple(filter(inner, tup))
