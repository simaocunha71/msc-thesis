def tuple_intersection(lst1, lst2):
    # Convert the tuples in both lists to sets
    set1 = set(map(frozenset, lst1))
    set2 = set(map(frozenset, lst2))
    
    # Find the intersection of the two sets
    intersection = set1.intersection(set2)
    
    # Convert the sets back to tuples
    return set(map(tuple, intersection))