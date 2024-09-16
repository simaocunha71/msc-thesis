def find_dissimilar(tup1, tup2):
    return tuple(i for i in tup1 if i not in tup2) + tuple(i for i in tup2 if i not in tup1)