def unique_sublists(l):
    d={}
    for i in l:
        t=tuple(i)
        if t not in d:
            d[t]=0
        d[t]+=1
    return d