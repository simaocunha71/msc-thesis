def maximize_elements(test_tup1: tuple, test_tup2: tuple) -> tuple:
    max_elems = []
    for i in range(len(test_tup1)):
        if test_tup1[i] > test_tup2[i]:
            max_elems.append(test_tup1[i])
        else:
            max_elems.append(test_tup2[i])
    return tuple(max_elems)