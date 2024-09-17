def tuple_intersection(tuple_list, other_tuple_list):
    set1 = set(tuple_list)
    set2 = set(other_tuple_list)
    intersection = set1 & set2
    return tuple(sorted(intersection))