def index_multiplication(tup1, tup2):
    assert len(tup1) == len(tup2), "Tuples must be of the same length"
    return tuple(map(lambda x, y: (x[0] * y[0], x[1] * y[1]), tup1, tup2))