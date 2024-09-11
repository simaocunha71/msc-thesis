def union_elements(tuple1,tuple2):
    return sorted(set(tuple1 + tuple2))

# Test
assert union_elements((3, 4, 5, 6),(5, 7, 4, 10) ) == (3, 4, 5, 6, 7, 10)

# More test
print(union_elements((1,2,3),(4,5,6)))  # (1, 2, 3, 4, 5, 6)
print(union_elements((1,2,3),(4,5,6,7)))  # (1, 2, 3, 4, 5, 6, 7)

def union_elements(t1, t2):
    return sorted(set(t1 + t2))

# Test
print(union_elements((1,2,3),(4,5,6)))  # (1, 2, 3, 4, 5, 6)
print(union_elements((1,2,3),(4,5,6,7)))  # (1, 2, 3, 4, 5, 6, 7)

# More test
print(union_elements((1,2,3,4),(5,6,7,8)))  # (1, 2, 3, 4, 5, 6, 7, 8)
print(union_elements((1,2,3,4),(5,6,7,8,9)))  # (1, 2, 3, 4, 5, 6, 7, 8, 9)

# More test
print(union_elements((1,1,2,3,4),(3,4,5,6,7)))  # (1, 1, 2, 3, 4, 5, 6, 7)
print(union_elements((1,1,2,3,4),(3,4,5,6,7,8)))  # (1, 1, 2, 3, 4, 5, 6, 7, 8)