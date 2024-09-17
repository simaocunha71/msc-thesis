def unique_sublists(lst):
    dct = {}
    for sublist in map(tuple, lst):
        dct[sublist] = dct.get(sublist, 0) + 1
    return dct