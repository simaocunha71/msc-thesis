def frequency_lists(lst):
    d = {}
    for i in lst:
        for j in i:
            if j in d:
                d[j] += 1
            else:
                d[j] = 1
    return d