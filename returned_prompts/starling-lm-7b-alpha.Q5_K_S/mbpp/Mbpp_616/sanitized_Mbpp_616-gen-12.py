def tuple_modulo(test_tup1, test_tup2):
    return tuple(elem % elem_2 for elem, elem_2 in zip(test_tup1, test_tup2))