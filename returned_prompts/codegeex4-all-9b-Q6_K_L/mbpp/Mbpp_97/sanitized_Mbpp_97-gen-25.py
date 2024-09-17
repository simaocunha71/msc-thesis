def frequency_lists(lst):
    d = {}
    for sublist in lst:
        for item in sublist:
            if item in d:
                d[item] += 1
            else:
                d[item] = 1
    return d