def add_lists(list1: list, tup1: tuple) -> tuple:
    list1.extend(tup1)
    return tuple(list1)