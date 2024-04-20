"""
Write a python function to remove duplicate numbers from a given number of lists.
assert two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]
"""

def two_unique_nums(lists):
    if type(lists[0]) is not list:
        raise TypeError('lists must be a list object')

    n = len(lists)
    unique_nums = []
    for i in range(n):
        if unique_nums.count(lists[i][0]):
            del lists[i]
        else:
            unique_nums.append(lists[i])
    return [unique_nums, n]
