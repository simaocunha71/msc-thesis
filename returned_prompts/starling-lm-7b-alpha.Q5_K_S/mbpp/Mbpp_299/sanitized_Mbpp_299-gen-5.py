def max_aggregate(t):
    d={}
    for i in t:
        if i[0] in d:
            d[i[0]]+=i[1]
        else:
            d[i[0]]=i[1]
    return max(d.items(), key=lambda x:x[1])