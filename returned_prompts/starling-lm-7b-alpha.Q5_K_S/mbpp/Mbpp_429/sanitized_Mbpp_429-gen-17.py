def and_tuples(test_tup1, test_tup2):
    return tuple(min(i,j) for i,j in zip(test_tup1, test_tup2))