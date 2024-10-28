
def remove_nested(t):
    for i, e in enumerate(t):
        if isinstance(e, tuple):
            t = t[:i] + t[i+1:]
            break
    return t


