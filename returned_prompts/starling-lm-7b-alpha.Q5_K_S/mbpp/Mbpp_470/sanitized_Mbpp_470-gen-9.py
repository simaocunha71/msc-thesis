def add_pairwise(tup):
    res = []
    for i in range(len(tup)-1):
        res.append(tup[i]+tup[i+1])
    res.append(tup[-1]+tup[-2])
    return tuple(res)