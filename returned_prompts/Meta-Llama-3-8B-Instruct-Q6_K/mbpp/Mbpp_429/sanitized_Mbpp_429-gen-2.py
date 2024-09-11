def and_tuples(tup1, tup2):
    return tuple(a & b for a, b in zip(tup1, tup2))