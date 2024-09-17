def tuple_modulo(t1, t2):
    l1 = len(t1)
    l2 = len(t2)
    assert l1 == l2, "length of tuples should be same"
    res = []
    for i in range(l1):
        res.append(t1[i]%t2[i])
    return tuple(res)