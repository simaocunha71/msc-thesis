def find_dissimilar(tup1, tup2):
    dissimilar = list(set(tup1) ^ set(tup2))
    return tuple(dissimilar)