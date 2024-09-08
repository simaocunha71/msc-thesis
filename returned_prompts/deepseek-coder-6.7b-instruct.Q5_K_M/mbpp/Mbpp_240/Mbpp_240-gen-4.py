def replace_list(l1,l2):
    l1[-1] = l2
    return l1

l1 = [1, 3, 5, 7, 9, 10]
l2 = [2, 4, 6, 8]

print(replace_list(l1,l2))

"""
Output:
[1, 3, 5, 7, 9, [2, 4, 6, 8]]
"""

