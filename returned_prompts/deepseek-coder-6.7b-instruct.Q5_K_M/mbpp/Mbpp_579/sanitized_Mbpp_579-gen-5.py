def find_dissimilar(t1, t2):
    d = dict()
    for i in t1:
        d[i] = d.get(i, 0) + 1
    for i in t2:
        d[i] = d.get(i, 0) + 1
    return tuple(i for i in d if d[i] == 1)