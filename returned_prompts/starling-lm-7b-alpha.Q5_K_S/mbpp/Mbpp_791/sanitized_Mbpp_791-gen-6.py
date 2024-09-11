def remove_nested(t):
    if isinstance(t, tuple):
        return tuple(remove_nested(i) for i in t if not isinstance(i, tuple))
    else:
        return t