def division_elements(tup1, tup2):
    return tuple(i / j for i, j in zip(tup1, tup2))  # Python 3.x
    # return tuple(map(lambda x, y: x / y, tup1, tup2))  # Python 2.x