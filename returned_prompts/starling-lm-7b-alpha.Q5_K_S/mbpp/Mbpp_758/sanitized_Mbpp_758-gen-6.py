def unique_sublists(mylist):
    d={}
    for l in mylist:
        tup=tuple(l)
        if tup in d:
            d[tup]+=1
        else:
            d[tup]=1
    return d