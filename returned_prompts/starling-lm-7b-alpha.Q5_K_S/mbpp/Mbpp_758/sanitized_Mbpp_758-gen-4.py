def unique_sublists(l):
    s = set()
    d = {}
    for i in l:
        t = tuple(i)
        if t in s:
            d[t] += 1
        else:
            s.add(t)
            d[t] = 1
    return d