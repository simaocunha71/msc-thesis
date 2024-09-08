from itertools import product

def combinations_colors(lst, n):
    return [x for x in product(lst, repeat=n)]

print(combinations_colors(["Red","Green","Blue"],1))

"""
Output:
[('Red',), ('Green',), ('Blue',)]
"""

"""
