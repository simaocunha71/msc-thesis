def index_multiplication(t1,t2):
    l1 = len(t1)
    l2 = len(t2)
    l = min(l1,l2)
    res = []
    for i in range(l):
        res.append((t1[i][0]*t2[i][0],t1[i][1]*t2[i][1]))
    return tuple(res)