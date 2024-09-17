def tuple_intersection(tuple_list1, tuple_list2):
    set1 = set(tuple1 for tuple1 in tuple_list1)
    set2 = set(tuple2 for tuple2 in tuple_list2)
    intersection = set1 & set2
    return intersection