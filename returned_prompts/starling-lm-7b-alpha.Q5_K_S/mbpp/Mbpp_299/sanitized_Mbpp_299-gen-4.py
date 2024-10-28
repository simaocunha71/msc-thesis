def max_aggregate(tup):
    l = []
    for i in tup:
        if i[0] not in l:
            l.append(i[0])
    res = []
    for i in l:
        res.append(tup[tup.index(i)+1:].index(max(tup,key = lambda x:x[1])))
    return max(tup,key = lambda x:x[1]),sum(res)