def union_elements(tup1, tup2):
    result = list(set(tup1 + tup2))
    result.sort()
    return tuple(result)