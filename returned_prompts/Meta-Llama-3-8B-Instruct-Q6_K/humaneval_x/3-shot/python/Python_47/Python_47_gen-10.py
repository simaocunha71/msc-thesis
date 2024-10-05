    l.sort()
    length = len(l)
    mid = length // 2

    if length % 2 == 0:
        return (l[mid - 1] + l[mid]) / 2
    else:
        return l[mid]  # or l[mid - 1] if you want to round down


