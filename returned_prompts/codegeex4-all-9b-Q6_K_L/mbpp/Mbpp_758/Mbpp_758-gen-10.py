def unique_sublists(lst):
    unique_sublists_dict = {}
    for sublist in lst:
        sublist_tuple = tuple(sublist)
        if sublist_tuple in unique_sublists_dict:
            unique_sublists_dict[sublist_tuple] += 1
        else:
            unique_sublists_dict[sublist_tuple] = 1
    return unique_sublists_dict

