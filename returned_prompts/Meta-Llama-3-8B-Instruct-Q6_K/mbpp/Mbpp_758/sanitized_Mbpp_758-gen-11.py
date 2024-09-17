def unique_sublists(lst):
    seen = set()
    count_dict = {}
    for sublist in lst:
        tuple_sublist = tuple(sublist)
        if tuple_sublist in seen:
            count_dict[tuple_sublist] += 1
        else:
            seen.add(tuple_sublist)
            count_dict[tuple_sublist] = 1
    return count_dict