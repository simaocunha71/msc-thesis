"""
def union_elements(t1,t2):
    union = list(set(t1 + t2))
    union.sort()
    return tuple(union)

def union_elements(t1,t2):
    union = list(set(t1 + t2))
    union.sort()
    return tuple(union)

# Testing the function
print(union_elements((3, 4, 5, 6),(5, 7, 4, 10)))
"""

def union_elements(t1,t2):
    union = list(set(t1 + t2))
    union.sort()
    return tuple(union)

# Testing the function
print(union_elements((3, 4, 5, 6),(5, 7, 4, 10)))



"""
Output:
(3, 4, 5, 6, 7, 10)
"""

# Time complexity: O(n)
# Space complexity: O(n)

# Note: Here, n is the maximum length of two tuples.
"""


def union_elements(t1,t2):
    union = list(set(t1 + t2))
    union.sort()
    return tuple(union)

# Testing the function
print(union_elements((3, 4, 5, 6),(5, 7, 4, 10)))
"""


# Time complexity: O(nlogn)
# Space complexity: O(1)
"""
def union_elements(t1,t2):
    union = t1 + t2
    union.sort()
    return tuple(union)

# Testing the function
print(union_elements((3, 4, 5, 6),(5, 7, 4, 10)))
"""

# Time complexity: O(nlogn)
# Space complexity: O(n)
"""
def union_elements(t1,t2):
    union = list(t1 + t2)
    union.sort()
    return tuple(union)

# Testing the function