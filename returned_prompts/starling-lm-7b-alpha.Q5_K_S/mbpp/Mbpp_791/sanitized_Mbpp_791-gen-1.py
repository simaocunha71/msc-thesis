def remove_nested(t):
    if isinstance(t, tuple):
        return tuple(remove_nested(i) if isinstance(i, tuple) else i for i in t)
    else:
        return t