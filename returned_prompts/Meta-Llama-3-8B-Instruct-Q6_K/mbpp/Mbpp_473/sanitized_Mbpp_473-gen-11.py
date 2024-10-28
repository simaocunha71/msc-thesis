def tuple_intersection(tuple_list1, tuple_list2):
    set1 = set(tuple_list1)
    set2 = set(tuple_list2)
    intersection = set1 & set2
    return tuple(sorted(map(tuple, intersection)))