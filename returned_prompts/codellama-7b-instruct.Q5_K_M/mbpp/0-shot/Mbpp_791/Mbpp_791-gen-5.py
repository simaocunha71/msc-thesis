def remove_nested(t):
    if len(t) == 1:
        return t
    elif len(t) > 1 and isinstance(t[-1], tuple):
        return t[:-1] + remove_nested(t[-1])
    else:
        return t
