def unique_sublists(lst):
    unique_sublists = {}
    for sublist in lst:
        sublist = tuple(sublist)
        if sublist in unique_sublists:
            unique_sublists[sublist] += 1
        else:
            unique_sublists[sublist] = 1
    return unique_sublists
