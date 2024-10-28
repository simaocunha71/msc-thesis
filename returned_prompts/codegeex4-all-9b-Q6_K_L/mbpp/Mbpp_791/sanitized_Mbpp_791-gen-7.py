def remove_nested(t):
    new_t = []
    for i in t:
        if isinstance(i, tuple):
            new_t.append(remove_nested(i))
        else:
            new_t.append(i)
    return tuple(new_t)