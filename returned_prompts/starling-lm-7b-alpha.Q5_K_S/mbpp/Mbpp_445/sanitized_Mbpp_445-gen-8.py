def index_multiplication(t1, t2):
    res = []
    for i in range(len(t1)):
        res.append((t1[i]*t2[i]))
    return tuple(res)
t1 = (1, 3, 4, 5, 2, 9, 1, 10)
t2 = (6, 7, 3, 9, 1, 1, 7, 3)