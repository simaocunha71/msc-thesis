def union_elements(t1, t2):
    return tuple(sorted(set(t1) | set(t2)))

print(union_elements((3, 4, 5, 6),(5, 7, 4, 10)))

