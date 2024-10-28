def add_pairwise(tup):
    return tuple(tup[i+1]+tup[i] for i in range(len(tup)-1))