def unique_sublists(l):
    d = {}
    for i in l:
        d[tuple(i)] = d.get(tuple(i), 0) + 1
    return d