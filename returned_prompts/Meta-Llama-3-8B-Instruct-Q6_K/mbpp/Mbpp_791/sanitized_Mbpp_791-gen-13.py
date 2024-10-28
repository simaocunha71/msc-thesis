def remove_nested(t):
    new_t = ()
    for item in t:
        if isinstance(item, tuple):
            continue
        new_t += (item,)
    return new_t