def division_elements(tup1, tup2):
    res = []
    for i in range(len(tup1)):
        res.append(tup1[i] / tup2[i])
    return tuple(res)