def remove_nested(t):
    return tuple(i for i in t if not isinstance(i, tuple))