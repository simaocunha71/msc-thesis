def and_tuples(test_tup1, test_tup2):
    return tuple(map(lambda x: x[0] & x[1], zip(test_tup1, test_tup2)))

