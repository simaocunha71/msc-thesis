    d = {}
    for elem in lst:
        if elem not in d:
            d[elem] = 0
        d[elem] += 1

    for key in d:
        if d[key] >= key:
            return key

    return -1


