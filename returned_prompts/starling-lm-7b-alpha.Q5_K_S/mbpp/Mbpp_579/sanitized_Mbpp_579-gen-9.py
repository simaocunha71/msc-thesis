def find_dissimilar(t1, t2):
    set1 = set(t1)
    set2 = set(t2)
    return tuple(set2-set1)