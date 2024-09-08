def find_dissimilar(t1, t2):
    set1, set2 = set(t1), set(t2)
    return tuple(set1 ^ set2)