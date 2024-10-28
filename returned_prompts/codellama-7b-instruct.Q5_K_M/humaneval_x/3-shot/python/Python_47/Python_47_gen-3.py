    l = sorted(l)
    if len(l) % 2 == 0:
        return (l[int(len(l) / 2)] + l[int((len(l) / 2) - 1)]) / 2
    else:
        return l[int(len(l) / 2)]


