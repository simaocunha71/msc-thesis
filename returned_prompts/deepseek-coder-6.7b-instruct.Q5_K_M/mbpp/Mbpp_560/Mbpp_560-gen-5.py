def union_elements(t1, t2):
    union = t1 + t2
    return tuple(sorted(union))

print(union_elements((3, 4, 5, 6),(5, 7, 4, 10)))

"""
