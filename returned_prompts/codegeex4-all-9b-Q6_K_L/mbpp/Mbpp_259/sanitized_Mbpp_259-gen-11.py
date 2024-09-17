def maximize_elements(tup1, tup2):
    return tuple(max(tup1[i], tup2[i]) for i in range(len(tup1)))