    d = {}

    for i in test.split():
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    return d


