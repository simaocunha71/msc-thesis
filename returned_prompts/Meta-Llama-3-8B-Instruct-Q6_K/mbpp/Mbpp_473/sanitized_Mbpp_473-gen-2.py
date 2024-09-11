def tuple_intersection(tuples1, tuples2):
    set1 = set(map(frozenset, tuples1))
    set2 = set(map(frozenset, tuples2))
    return [frozenset(t) for t in (set1 & set2)]