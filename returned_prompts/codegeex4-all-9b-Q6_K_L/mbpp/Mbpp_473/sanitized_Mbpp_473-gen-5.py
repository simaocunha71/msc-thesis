def tuple_intersection(list1, list2):
    common_elements = set()
    for t1 in list1:
        for t2 in list2:
            if set(t1) == set(t2):
                common_elements.add(tuple(sorted(t1)))
    return common_elements