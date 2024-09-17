def union_elements(t1, t2):
    union = set(t1) | set(t2)
    union = sorted(union)
    return tuple(union)