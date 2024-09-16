def add_pairwise(my_tuple):
    return tuple(a + b for a, b in zip(my_tuple, my_tuple[1:]))