def tuple_modulo(test_tup1, test_tup2):
    return tuple(map(lambda x,y: (x-y) % y, test_tup1, test_tup2))