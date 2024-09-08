def find_dissimilar(t1, t2):
    return tuple(set(t1) ^ set(t2))