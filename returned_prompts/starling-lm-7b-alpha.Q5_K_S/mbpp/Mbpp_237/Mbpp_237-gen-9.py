def sum_dict(l):
    d={}
    for i in l:
        for j in i:
            if j not in d:
                d[j]=i[j]
            else:
                d[j]+=i[j]
    return d

"""
