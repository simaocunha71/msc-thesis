def unique_sublists(lst):
    count_dict = {}
    for sublist in lst:
        tuple_sublist = tuple(sublist)
        if tuple_sublist in count_dict:
            count_dict[tuple_sublist] += 1
        else:
            count_dict[tuple_sublist] = 1
    return count_dict