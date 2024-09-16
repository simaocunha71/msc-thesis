def add_pairwise(my_tuple):
    return tuple(map(sum, zip(my_tuple, my_tuple[1:])))
