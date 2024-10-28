def maximize_elements(tup1, tup2):
    return tuple(map(lambda x, y: (max(x[0], y[0]), max(x[1], y[1])), tup1, tup2))