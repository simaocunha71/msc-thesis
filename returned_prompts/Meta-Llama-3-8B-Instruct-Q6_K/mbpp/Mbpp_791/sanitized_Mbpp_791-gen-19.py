def remove_nested(t):
    new_t = []
    for elem in t:
        if isinstance(elem, tuple):
            new_t.extend(remove_nested(elem))
        else:
            new_t.append(elem)
    return tuple(new_t)