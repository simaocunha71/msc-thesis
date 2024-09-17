def maximize_elements(tup1, tup2):
    res = []
    for i in range(len(tup1)):
        res.append((max(tup1[i][0], tup2[i][0]), max(tup1[i][1], tup2[i][1])))
    return tuple(res)