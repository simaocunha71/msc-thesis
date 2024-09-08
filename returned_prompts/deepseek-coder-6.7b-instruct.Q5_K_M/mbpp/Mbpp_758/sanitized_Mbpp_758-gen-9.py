def unique_sublists(lst):
    count = {}
    for sublist in lst:
        tuple_sublist = tuple(sublist)
        if tuple_sublist in count:
            count[tuple_sublist] += 1
        else:
            count[tuple_sublist] = 1
    return count