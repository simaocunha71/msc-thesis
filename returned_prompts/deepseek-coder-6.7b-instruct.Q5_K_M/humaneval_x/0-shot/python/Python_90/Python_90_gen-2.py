
def next_smallest(lst):
    if len(lst) < 2:
        return None
    lst = list(set(lst))
    lst.sort()
    return lst[1] if len(lst) > 1 else None


print(next_smallest([1, 2, 3, 4, 5]))  # 2
print(next_smallest([5, 1, 4, 3, 2]))  # 2
print(next_smallest([]))  # None
print(next_smallest([1, 1]))  # None


Explanation:

This function first checks if the list has less than 2 elements. If it does, it returns None because a list with less than 2 unique elements cannot have a second smallest element. 

It then converts the list to a set to remove any duplicate elements, then converts it back to a list. The list is then sorted in ascending order. 

If the list has at least 2 elements, it returns the second element in the list (0-indexed). If the list has only 1 element, it returns None as there is no second smallest element.
"""

# Solution 2
def next_smallest(lst):
    if len(lst) < 2:
        return None
    smallest = second_smallest = float('inf')
    for num in lst:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num
    return None if second_smallest == float('inf') else second_smallest


print(next_smallest([1, 2, 3, 4, 5]))  # 2
print(next_smallest([5, 1, 4, 3, 2]))  # 2
print(next_smallest([]))  # None
print(next_smallest([1, 1]))  # None

"""
Explanation:

This function first checks if the list has less than 2 elements. If it does, it returns None because a list with less than 2