def index_multiplication(tup1, tup2):
    res = []
    for a, b in zip(tup1, tup2):
        res.append(tuple(i * j for i, j in zip(a, b)))
    return tuple(res)