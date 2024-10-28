def index_multiplication(tuple1, tuple2):
    return tuple(map(lambda x: tuple(map(lambda y: x[0]*y[0], x)), zip(tuple1, tuple2)))