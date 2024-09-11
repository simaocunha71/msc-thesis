def remove_nested(tup):
    return tuple(x for x in tup if not isinstance(x, tuple))
    # or return tuple(x for x in tup if not isinstance(x, tuple)) if you want to keep the order of the elements