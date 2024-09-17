
def index_multiplication(tup1, tup2):
    return tuple(tuple(i*j for i, j in zip(x, y)) for x, y in zip(tup1, tup2))


