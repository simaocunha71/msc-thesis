def find_dissimilar(test_tup1, test_tup2):
    return tuple([i for i in test_tup1 + test_tup2 if test_tup1.count(i) != test_tup2.count(i)])