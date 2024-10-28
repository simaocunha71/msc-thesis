def unique_sublists(lst):
    unique = {}
    for sublist in lst:
        unique[tuple(sublist)] = unique.get(tuple(sublist), 0) + 1
    return unique