def remove_nested(t):
    for i in range(len(t)):
        if isinstance(t[i], tuple):
            t = t[:i] + t[i+1:]
    return t