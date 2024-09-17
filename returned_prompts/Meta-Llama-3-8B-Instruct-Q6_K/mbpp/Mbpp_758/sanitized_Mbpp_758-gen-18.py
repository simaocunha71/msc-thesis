def unique_sublists(lst):
    result = {}
    for sublst in lst:
        sublst = tuple(sublst)
        if sublst in result:
            result[sublst] += 1
        else:
            result[sublst] = 1
    return result