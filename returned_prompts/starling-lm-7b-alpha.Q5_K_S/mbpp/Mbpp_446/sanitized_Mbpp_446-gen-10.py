def count_Occurrence(t,l):
    res = {}
    for i in l:
        if i in res:
            res[i] += 1
        else:
            res[i] = 1
    for i in t:
        if i in res:
            res[i] += 1
        else:
            res[i] = 1
    return res