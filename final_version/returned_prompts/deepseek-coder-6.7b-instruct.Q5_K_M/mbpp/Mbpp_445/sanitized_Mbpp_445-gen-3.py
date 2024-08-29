def index_multiplication(tuples):
    t1, t2 = tuples
    res = []
    for i in range(len(t1)):
        res.append(tuple(map(lambda x, y: x*y, t1[i], t2[i])))
    return tuple(res)