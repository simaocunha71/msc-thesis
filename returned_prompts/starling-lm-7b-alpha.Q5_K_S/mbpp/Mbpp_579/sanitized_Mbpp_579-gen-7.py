def find_dissimilar(tup1, tup2):
    return list(set(tup1) - set(tup2)) + list(set(tup2) - set(tup1))