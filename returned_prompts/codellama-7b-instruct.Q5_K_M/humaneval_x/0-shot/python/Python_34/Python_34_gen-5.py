
    l.sort()
    n = len(l)
    for i in range(n-1):
        if l[i] == l[i+1]:
            l.pop(i+1)
    return l
