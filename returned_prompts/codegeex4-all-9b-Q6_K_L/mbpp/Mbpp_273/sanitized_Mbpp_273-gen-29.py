def substract_elements(tup1, tup2):
    return tuple(t1 - t2 for t1, t2 in zip(tup1, tup2))