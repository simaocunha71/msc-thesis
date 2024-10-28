
def index_multiplication(tup1, tup2):
    return tuple(tuple(x*y for x, y in zip(tup1[i], tup2[i])) for i in range(len(tup1)))


