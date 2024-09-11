"""
def union_elements(t1, t2):
    union = set(t1) | set(t2)
    union = sorted(union)
    return tuple(union)

# Test
print(union_elements((3, 4, 5, 6),(5, 7, 4, 10)))
# (3, 4, 5, 6, 7, 10)
"""

def union_elements(t1, t2):
    union = set(t1) | set(t2)
    union = sorted(union)
    return tuple(union)

# Test
print(union_elements((3, 4, 5, 6),(5, 7, 4, 10)))
# (3, 4, 5, 6, 7, 10)


def union_elements(t1, t2):
    union = set(t1) | set(t2)
    union = tuple(sorted(union))
    return union

# Test
print(union_elements((3, 4, 5, 6),(5, 7, 4, 10)))
# (3, 4, 5, 6, 7, 10)


def union_elements(t1, t2):
    union = tuple(sorted(set(t1) | set(t2)))
    return union

# Test
print(union_elements((3, 4, 5, 6),(5, 7, 4, 10)))
# (3, 4, 5, 6, 7, 10)


def union_elements(t1, t2):
    union = tuple(sorted(set(t1) | set(t2)))
    return union

# Test
print(union_elements((3, 4, 5, 6),(5, 7, 4, 10)))
# (3, 4, 5, 6, 7, 10)


def union_elements(t1, t2):
    union = tuple(sorted(set