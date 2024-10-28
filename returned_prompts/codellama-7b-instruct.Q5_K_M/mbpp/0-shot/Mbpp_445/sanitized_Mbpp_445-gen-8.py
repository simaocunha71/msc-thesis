def index_multiplication(tup1, tup2):
    return tuple(map(lambda x: x[0] * x[1], zip(tup1, tup2)))