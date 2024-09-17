def unique_sublists(lst):
    unique_sublists = {}
    for sublist in lst:
        tuple_sublist = tuple(sublist)
        if tuple_sublist in unique_sublists:
            unique_sublists[tuple_sublist] += 1
        else:
            unique_sublists[tuple_sublist] = 1
    return unique_sublists