    l.sort()
    length = len(l)

    if length % 2 == 0:
        return (l[length // 2 - 1] + l[length // 2]) / 2

    return l[length // 2]


