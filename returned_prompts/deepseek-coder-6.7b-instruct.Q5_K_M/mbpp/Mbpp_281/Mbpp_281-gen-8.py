def all_unique(lst):
    return len(lst) == len(set(lst))

print(all_unique([1,2,3])) # True
print(all_unique([1,1,2])) # False

"""
Explanation:
The function all_unique checks if the length of the given list is equal to the length of the set of the list. The set function removes any duplicate elements from the list, and if all elements are unique, this will result in a list of the same length as the original. If there were any duplicate elements, the length of the set would be shorter than the length of the original list.
"""

