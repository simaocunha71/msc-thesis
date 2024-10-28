def index_multiplication(tuples):
    tup1, tup2 = tuples
    res = []
    for i in range(len(tup1)):
        res.append(tuple([tup1[i][j] * tup2[i][j] for j in range(len(tup1[i]))]))
    return tuple(res)