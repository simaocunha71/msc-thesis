def tuple_intersection(tuples1, tuples2):
    set1 = set(tuple(sorted(t)) for t in tuples1)
    set2 = set(tuple(sorted(t)) for t in tuples2)
    return set1 & set2