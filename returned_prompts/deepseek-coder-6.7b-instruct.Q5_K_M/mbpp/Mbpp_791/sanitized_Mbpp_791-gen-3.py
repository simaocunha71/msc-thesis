def remove_nested(tup):
    return tuple(i for i in tup if not isinstance(i, tuple))