def replace_list(list1, list2):
    list1.pop()
    list1.extend(list2)
    return list1

print(replace_list([1, 3, 5, 7, 9, 10],[2, 4, 6, 8]))

"""
Output:
[1, 3, 5, 7, 9, 2, 4, 6, 8]
"""

