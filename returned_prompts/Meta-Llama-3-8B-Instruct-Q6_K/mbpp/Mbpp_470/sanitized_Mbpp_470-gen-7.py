def add_pairwise(tup):
    return tuple(sum(pair) for pair in zip(tup, tup[1:]))