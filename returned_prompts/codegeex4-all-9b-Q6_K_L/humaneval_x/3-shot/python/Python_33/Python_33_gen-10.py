    l = l.copy()

    for idx in range(len(l)):
        if idx % 3 == 0:
            l[idx] = sorted(l[idx::3])

    return l

