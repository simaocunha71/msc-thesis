    counter = {}
    for n in lst:
        if n in counter:
            counter[n] += 1
        else:
            counter[n] = 1

    for k, v in counter.items():
        if k >= v:
            return k

    return -1

