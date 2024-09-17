
def add_pairwise(tup):
    return tuple(map(sum, zip(tup[0::2], tup[1::2])))


