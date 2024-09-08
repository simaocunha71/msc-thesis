def find_dissimilar(t1, t2):
    return tuple(set(t1).symmetric_difference(set(t2)))