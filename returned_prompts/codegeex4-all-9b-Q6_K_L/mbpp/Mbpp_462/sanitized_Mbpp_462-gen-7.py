def combinations_list(lst):
    res = [[]]
    for i in range(len(lst)):
        res += [[lst[i]] + sub for sub in res]
    return res