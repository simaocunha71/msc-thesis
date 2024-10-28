def remove_nested(tup):
    if isinstance(tup, tuple):
        return remove_nested(tup[0])
    else:
        return tup
