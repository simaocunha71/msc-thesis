def index_multiplication(tup1, tup2):
    return tuple(map(lambda x,y: (x*y[0], y[1]), tup1, tup2))