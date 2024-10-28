def unique_sublists(lst):
    result = {}
    for sublist in lst:
        if isinstance(sublist, list):
            sublist = tuple(sublist)
        if sublist in result:
            result[sublist] += 1
        else:
            result[sublist] = 1
    return result