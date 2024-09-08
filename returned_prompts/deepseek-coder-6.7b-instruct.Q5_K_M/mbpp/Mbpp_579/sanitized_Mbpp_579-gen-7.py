def find_dissimilar(t1, t2):
    return tuple(x for x in t1 if x not in t2) + tuple(x for x in t2 if x not in t1)