def combinations_list(lst):
    res = [[]]
    for i in range(len(lst)):
        res += [x + [lst[i]] for x in res]
    return res