    l = list(l)
    indices = [i for i in range(len(l)) if i % 3 == 0]
    l[indices] = sorted(l[indices])
    return l

