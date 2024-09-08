def merge_sorted_list(list1, list2, list3):
    result = []
    result.extend(list1)
    result.extend(list2)
    result.extend(list3)
    result.sort()
    return result

print(merge_sorted_list([25, 24,_list([15, 4, 5, 29, 110]),[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48]))
"""
"""


def merge_sorted_list(list1, list2, list3):
    result = []
    result.extend(list1)
    result.extend(list2)
    result.extend(list3)
    result.sort()
    return result

print(merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48]))
assert merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48])==[4, 5, 11, 15, 19, 20, 24, 24, 25, 25, 26, 29, 48, 54, 56, 110, 154, 233]
"""
The function merge_sorted_list(list1, list2, list3) takes in three lists, list1, list2, and list3. 
The extend() method adds the elements of list2 and list3 to the end of the list1.
The sort()