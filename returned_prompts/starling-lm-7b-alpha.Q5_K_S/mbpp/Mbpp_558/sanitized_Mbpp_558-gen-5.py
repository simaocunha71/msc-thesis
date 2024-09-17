def digit_distance_nums(n, m):
    nd = str(n)
    md = str(m)
    if len(nd) != len(md):
        return False
    else:
        ndigits = len(nd)
        res = 0
        for i in range(ndigits):
            res += abs(int(nd[i]) - int(md[i]))
    return res