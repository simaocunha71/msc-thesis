def dict_filter(d,n):
    new_d={}
    for i in d:
        if d[i]>=n:
            new_d[i]=d[i]
    return new_d