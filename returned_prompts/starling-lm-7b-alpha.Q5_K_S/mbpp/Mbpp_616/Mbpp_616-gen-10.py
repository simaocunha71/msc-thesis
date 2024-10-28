
def tuple_modulo(test_tup1, test_tup2):
    return tuple(elem % mod for elem, mod in zip(test_tup1, test_tup2))


