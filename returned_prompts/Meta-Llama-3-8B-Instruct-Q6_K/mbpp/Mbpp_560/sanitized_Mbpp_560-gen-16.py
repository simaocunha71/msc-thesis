def union_elements(tuple1, tuple2):
    set1 = set(tuple1)
    set2 = set(tuple2)
    union = set1.union(set2)
    return tuple(sorted(union))