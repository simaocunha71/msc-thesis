def tuple_modulo(test_tup1, test_tup2):
    return tuple(i % j for i, j in zip(test_tup1, test_tup2))