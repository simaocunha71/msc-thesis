    l = sorted(l)
    length = len(l)
    if length % 2 == 0:
        return (l[length // 2] + l[length // 2 - 1]) / 2.0
    else:
        return l[length // 2]


