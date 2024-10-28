
def add_pairwise(tup: tuple) -> tuple:
    return tuple(sum(x) for x in zip(tup, tup[1:]))


