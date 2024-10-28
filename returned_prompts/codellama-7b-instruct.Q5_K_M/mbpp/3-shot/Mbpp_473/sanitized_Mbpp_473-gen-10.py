def tuple_intersection(tuple_list1,tuple_list2):
    return set((tuple(sorted(tup)) for tup in tuple_list1)).intersection(set((tuple(sorted(tup)) for tup in tuple_list2)))