def and_tuples(tup1, tup2):
    return tuple(int(i & j) for i, j in zip(tup1, tup2))