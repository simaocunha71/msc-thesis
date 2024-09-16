def pack_consecutive_duplicates(lst):
    res = []
    for k, g in itertools.groupby(lst):
        res.append(list(g))
    return res
