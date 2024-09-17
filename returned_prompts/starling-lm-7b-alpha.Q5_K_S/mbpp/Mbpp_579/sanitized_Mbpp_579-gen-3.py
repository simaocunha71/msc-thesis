def find_dissimilar(t1, t2):
    t1 = set(t1)
    t2 = set(t2)
    dissimilar = t1 ^ t2
    return tuple(dissimilar)