def unique_sublists(l):
    d={}
    for i in l:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    for k,v in d.items():
        if isinstance(k,list):
            d[tuple(k)]=v
    return d