def index_multiplication(tuple1, tuple2):
    return tuple(tuple(x*y) for x, y in zip(tuple1, tuple2))