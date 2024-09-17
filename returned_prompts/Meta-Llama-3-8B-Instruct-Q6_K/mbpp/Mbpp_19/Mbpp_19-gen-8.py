```
def has_duplicates(nums):
    return len(nums) != len(set(nums))
```
The function `has_duplicates` takes a list of integers as input and returns a boolean value indicating whether the list contains any duplicate element or not.

The function works by comparing the length of the input list with the length of a set created from the input list. In Python, a set is an unordered collection of unique elements. If the lengths are equal, it means that the set (which contains no duplicate elements) has the same number of elements as the original list, which means that there are no duplicate elements in the list. If the lengths are not equal, it means that the set has fewer elements than the original list, which means that there are duplicate elements in the list.

The unit test `assert test_duplicate(([1,2,3,4,5]))==False` suggests that the function should return `False` for a list of distinct elements. This is consistent with the function's behavior, as it correctly identifies the list as not containing any duplicate elements.

Here's how you can use this function:
```
print(has_duplicates([1,2,3,4,5])) # Returns: False
print(has_duplicates([1,2,3,4,4])) # Returns: True
```



