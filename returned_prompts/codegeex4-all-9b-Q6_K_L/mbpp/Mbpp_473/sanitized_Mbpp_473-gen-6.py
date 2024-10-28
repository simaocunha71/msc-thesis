def tuple_intersection(tuple_list1, tuple_list2):
    # Convert each tuple to a set and find the intersection of all sets
    set_list1 = [set(t) for t in tuple_list1]
    set_list2 = [set(t) for t in tuple_list2]
    common_sets = set.intersection(*set_list1, *set_list2)
    
    # Convert the intersection of sets back to a set of tuples
    common_tuples = {tuple(sorted(s)) for s in common_sets}
    
    return common_tuples