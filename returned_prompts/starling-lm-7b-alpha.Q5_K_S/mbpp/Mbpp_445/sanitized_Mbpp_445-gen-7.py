def index_multiplication(t1,t2):
    len1 = len(t1)
    len2 = len(t2)
    if len1!=len2:
        return "Both tuples should be of same length"
    res = []
    for i in range(len1):
        res.append(t1[i]*t2[i])
    return tuple(res)