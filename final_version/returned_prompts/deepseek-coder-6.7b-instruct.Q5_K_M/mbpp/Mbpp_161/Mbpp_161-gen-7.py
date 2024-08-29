def remove_elements(lst1, lst2):
    for i in lst2:
        if i in lst1:
            lst1.remove(i)
    return lst1

print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]))  # [1, 3, 5, 7, 9, 10]
"""
This solution iterates over the second list and for each element checks if it exists in the first list. If it does, it removes it from the first list.

The time complexity of this solution is O(n^2) because for each element in the second list, it may need to iterate over the first list to find if it exists. The space complexity is O(1) as it uses a constant amount of extra space.
"""

# Another way to solve this problem is to use list comprehension and the in operator in python:

def remove_elements(lst1, lst2):
    return [i for i in lst1 if i not in lst2]

print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]))  # [1, 3, 5, 7, 9, 10]
"""
This solution uses list comprehension to create a new list that includes only the elements from the first list that are not in the second list.

The time complexity of this solution is O(n^2) because for each element in the first list, it may need to iterate over the second list to find if it exists. The space complexity is O(n) as it creates a new list.
"""

# Another way to solve this problem is to use the set data structure in python:

def remove_elements(lst1, lst2):
    return list(set(lst1) - set(lst2))

print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8,