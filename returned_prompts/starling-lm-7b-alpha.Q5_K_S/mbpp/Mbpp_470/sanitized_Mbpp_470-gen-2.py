def add_pairwise(t):
    res = []
    for i in range(len(t)-1):
        res.append(t[i]+t[i+1])
    res.append(t[-1]+t[0])
    return res