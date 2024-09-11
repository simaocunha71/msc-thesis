def tuple_intersection(tuples_list, other_tuples_list):
    set1 = set(map(tuple, tuples_list))
    set2 = set(map(tuple, other_tuples_list))
    return set1 & set2