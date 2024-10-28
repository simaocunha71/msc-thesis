def tuple_intersection(t1, t2):
    # Convert each tuple list to a set of unique elements
    s1 = set(t1)
    s2 = set(t2)
    
    # Find the intersection of the two sets
    intersection_set = s1 & s2
    
    # Convert the intersection set back to a tuple
    intersection_tuple = tuple(intersection_set)
    
    return intersection_tuple