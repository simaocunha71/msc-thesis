    l.sort()
    len_l = len(l)

    if len_l % 2 == 0:
        return (l[(len_l - 1) // 2] + l[len_l // 2]) / 2
    else:
        return l[len_l // 2]


