def add_lists(list1, tuple1):
    return tuple1 + tuple(list1) if isinstance(tuple1, tuple) else tuple1 + list(list1)