    l = sorted(l)

    if len(l) % 2 == 1:
        return l[len(l) // 2]

    mid = len(l) // 2
    return (l[mid - 1] + l[mid]) / 2


