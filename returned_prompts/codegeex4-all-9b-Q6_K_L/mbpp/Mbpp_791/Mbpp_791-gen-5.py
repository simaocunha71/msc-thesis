def remove_nested(tup):
    if isinstance(tup, tuple):
        return tuple(remove_nested(i) for i in tup if not isinstance(i, tuple))
    else:
        return tup

