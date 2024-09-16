def index_multiplication(tuple1, tuple2):
    assert len(tuple1) == len(tuple2)
    return tuple(map(lambda x, y: (x[0], x[1] * y[1]), tuple1, tuple2))
