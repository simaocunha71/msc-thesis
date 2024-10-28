
def index_multiplication(tup_a, tup_b):
    return tuple(map(lambda x, y: (x[0], x[1] * y[1]), tup_a, tup_b))


