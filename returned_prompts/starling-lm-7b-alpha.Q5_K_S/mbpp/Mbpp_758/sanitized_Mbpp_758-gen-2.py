def unique_sublists(lst):
    d = {}
    for i in lst:
        t = tuple(i)
        if t in d:
            d[t]+=1
        else:
            d[t]=1
    return d