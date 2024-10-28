def find_dissimilar(t1, t2):
    set1 = set(t1)
    set2 = set(t2)
    dissimilar = set1.symmetric_difference(set2)
    return tuple(dissimilar)