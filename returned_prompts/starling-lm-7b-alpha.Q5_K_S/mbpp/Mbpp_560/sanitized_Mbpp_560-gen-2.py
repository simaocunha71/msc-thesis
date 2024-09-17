def union_elements(t1,t2):
    union = list(set(t1 + t2))
    union.sort()
    return tuple(union)