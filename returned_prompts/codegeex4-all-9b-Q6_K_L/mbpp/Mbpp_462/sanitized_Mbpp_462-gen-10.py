def combinations_list(lst):
    res = [[]]
    for x in lst:
        res += [[x] + y for y in res]
    return res