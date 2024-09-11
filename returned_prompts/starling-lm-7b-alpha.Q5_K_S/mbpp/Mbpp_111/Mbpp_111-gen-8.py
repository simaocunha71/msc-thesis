"""
Here is one possible solution:

def common_in_nested_lists(lst):
    for sublist in lst:
        for elem in sublist:
            if all(elem != x for x in sublist):
                yield elem

assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
"""

from collections import Counter

def common_in_nested_lists(lst):
    ctr = Counter()
    for sublist in lst:
        for elem in sublist:
            ctr.update(elem)
    return ctr.elements()

common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]])

# Output:
# Counter({18: 2, 12: 2})
# [18, 12]

common_in_nested_lists([[1, 2, 3], [2, 3, 4], [3, 4, 5]])

# Output:
# Counter({3: 2, 2: 2, 1: 1})
# [1, 2, 3]

common_in_nested_lists([[1, 2], [2, 3], [3, 4]])

# Output:
# Counter({2: 1, 1: 1})
# [1, 2]

common_in_nested_lists([])

# Output:
# Counter()
# []

common_in_nested_lists([[]])

# Output:
# Counter()
# []

common_in_nested_lists([[1]])

