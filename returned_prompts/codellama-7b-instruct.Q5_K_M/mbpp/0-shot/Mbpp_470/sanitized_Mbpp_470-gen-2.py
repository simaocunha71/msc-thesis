def add_pairwise(tup):
    return tuple(map(sum, zip(tup, tup[1:])))