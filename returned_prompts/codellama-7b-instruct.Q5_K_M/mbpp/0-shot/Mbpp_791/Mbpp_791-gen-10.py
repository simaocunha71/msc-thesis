def remove_nested(t):
    if not t:
        return t
    if isinstance(t[0], tuple):
        return remove_nested(t[1:])
    return t[:1] + remove_nested(t[1:])
