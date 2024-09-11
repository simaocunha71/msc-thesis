def kth_element(nums, k):
    """
    Parameters:
    nums: a list of integers
    k: the kth element in the array
    Returns:
    the kth element in the array
    """
    return sorted(nums)[k-1]

# Testing
print(kth_element([12,3,5,7,19], 2))




















"""
To solve this problem, we can follow these steps:

1. Sort the given array using Python's built-in sorted function, which returns a new list containing all items from the original array in sorted order. This means that the kth element will be at index k-1 in the sorted list.

2. Return the kth element by indexing into the sorted list with k-1. Since Python uses 0-based indexing, we need to subtract 1 from k to get the correct index.

The time complexity of this solution is O(n log n) due to the sorting step, where n is the length of the input array. The space complexity is O(n), as the sorted list is a new list that needs to be stored.
"""

```python
def kth_element(nums, k):
    # Sort the given array in ascending order
    sorted_nums = sorted(nums)
    
    # Return the kth element by indexing into the sorted list with k-1
    return sorted_nums[k-1]
```

To test the function, we can use the provided assert statement:

```python
assert kth_element([12,3,5,7,19], 2) == 3
```

This will check if the function correctly returns the 2nd element in the array, which is 3.
```

```

```python
def kth_element(nums, k):
    """
    Parameters:
    nums: a list of integers
    k: the kth element in the array
    Returns:
    the kth element in the array
    """
    # Sort the given array in ascending order
