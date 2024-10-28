def tuple_to_dict(t):
    d = {}
    for i in range(len(t)-1):
        d[t[i]] = t[i+1]
    return d