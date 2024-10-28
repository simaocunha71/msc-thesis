def remove_nested(tup):
    if not tup:
        return tup
    if isinstance(tup[0], tuple):
        tup = tup[0] + tup[1:]
    return remove_nested(tup)
