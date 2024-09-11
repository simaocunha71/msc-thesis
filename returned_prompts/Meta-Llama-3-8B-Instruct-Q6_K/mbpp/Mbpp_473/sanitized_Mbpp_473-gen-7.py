def tuple_intersection(tup_list1, tup_list2):
    set1 = set(map(frozenset, tup_list1))
    set2 = set(map(frozenset, tup_list2))
    return [frozenset(t) for t in set1 & set2]  # return a list of frozensets