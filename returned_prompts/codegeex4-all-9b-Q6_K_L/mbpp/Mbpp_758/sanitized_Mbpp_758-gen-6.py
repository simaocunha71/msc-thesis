def unique_sublists(lst):
    counts = {}
    for sublist in lst:
        tuple_sublist = tuple(sublist)
        if tuple_sublist in counts:
            counts[tuple_sublist] += 1
        else:
            counts[tuple_sublist] = 1
    return counts