def unique_sublists(lst):
    sublists = [tuple(sublist) for sublist in lst]
    unique_sublists = set(sublists)
    result = {}
    for sublist in unique_sublists:
        result[sublist] = sublists.count(sublist)
    return result