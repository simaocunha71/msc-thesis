
def index_multiplication(tup1, tup2):
    return tuple(map(lambda x, y: (x[0], x[1] * y[1]), tup1, tup2))


