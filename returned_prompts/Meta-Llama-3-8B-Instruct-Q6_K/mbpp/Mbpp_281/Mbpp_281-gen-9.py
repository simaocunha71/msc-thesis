```
def all_unique(lst):
    return len(lst) == len(set(lst))
```
This function takes a list as an argument and returns a boolean indicating whether all elements in the list are unique or not. It does this by comparing the length of the list to the length of a set created from the list. In Python, a set is an unordered collection of unique elements. If the lengths are equal, it means that all elements in the list are unique, and the function returns True. Otherwise, it returns False.

For example, the unit test `assert all_unique([1,2,3]) == True` passes because the list [1,2,3] contains unique elements, so the function returns True.

Note that this function has a time complexity of O(n) because it needs to iterate over the entire list to create the set. This is more efficient than checking each element against every other element in the list, which would have a time complexity of O(n^2). However, for very large lists, creating a set may still be slow, and a more efficient algorithm would be needed.