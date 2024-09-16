def remove_nested(tup):
    if isinstance(tup[-1], tuple):
        tup = tup[:-1] + remove_nested(tup[-1])
    return tup