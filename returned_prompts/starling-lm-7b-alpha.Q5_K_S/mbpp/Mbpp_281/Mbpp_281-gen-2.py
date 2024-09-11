def all_unique(lst):
    return len(lst) == len(set(lst))

# Test
assert all_unique([1,2,3]) == True
assert all_unique([1,2,2]) == False
assert all_unique([]) == True




















"""
From the above, we can conclude that Python sets are unordered collections of unique elements.
This means that if we create a set from a list, it will remove any duplicate elements and keep only one of each.
We can use the len(set(lst)) function to check if all the elements in the list are unique or not.
This function will return the number of unique elements in the list.
If the number of unique elements is equal to the length of the list, this means that all the elements in the list are unique.
"""

"""
In the given function, we first convert the list into a set using set(lst) and then compare the length of the set with the length of the list using len(set(lst)) == len(lst).
If the lengths are equal, it means that all the elements in the list are unique and the function returns True. Otherwise, it returns False.
"""

"""
The time complexity of this function is O(n), where n is the length of the list.
This is because creating a set from a list takes O(n) time.
The set object itself does not have a time complexity associated with accessing elements, as it has a time complexity of O(1) for basic operations.
"""

"""
The space complexity of this function is also O(n), as creating a set requires additional memory to store the unique elements.
However, since sets are implemented as hash tables, the space complexity can be considered as O(k), where k is the number of unique elements in the list.
This is because a hash table requires space proportional to the number of unique elements, not the total number of elements in the list.
"""

"""
Overall, the given function is an efficient way to check if the elements of a given list are unique or not, with a time complexity of O(n) and a space complexity of O(n).
"""

"""
In conclusion, the function all_unique(lst) checks if