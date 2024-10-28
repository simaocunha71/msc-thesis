
def unique_sublists(lst: list):
    dct = {}
    for sublst in map(tuple, lst):
        dct[sublst] = dct.get(sublst, 0) + 1
    return dct


