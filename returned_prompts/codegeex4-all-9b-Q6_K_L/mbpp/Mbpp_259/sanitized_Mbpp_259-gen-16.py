def maximize_elements(test_tup1, test_tup2):
    test_tup1 = list(test_tup1)
    test_tup2 = list(test_tup2)
    for i in range(len(test_tup1)):
        test_tup1[i] = max(test_tup1[i], test_tup2[i])
    return tuple(test_tup1)