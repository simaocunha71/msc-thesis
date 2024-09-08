def unique_sublists(lst):
    sublist_dict = {}
    for sublist in lst:
        tuple_sublist = tuple(sublist)
        if tuple_sublist in sublist_dict:
            sublist_dict[tuple_sublist] += 1
        else:
            sublist_dict[tuple_sublist] = 1
    return sublist_dict