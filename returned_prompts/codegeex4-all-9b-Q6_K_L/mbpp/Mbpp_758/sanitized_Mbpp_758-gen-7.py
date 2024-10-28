def unique_sublists(lst):
    unique = {}
    for sublist in lst:
        tuple_sublist = tuple(sublist)
        if tuple_sublist in unique:
            unique[tuple_sublist] += 1
        else:
            unique[tuple_sublist] = 1
    return unique