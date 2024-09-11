"""
Here is a Python function to find the median of two sorted lists of same size:

```python
def get_median(list1, list2, size):
    merged_list = sorted(list1 + list2)
    return merged_list[size//2]
```

To test this function, you can use the assert statement to check if the result matches the expected result. For example, if the expected result is 16.0, you can write the assert statement as follows:

```python
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
```

This assert statement will pass if the median of the two lists is 16.0, and fail otherwise.
"""

# Python3 program to find median of two sorted lists

def get_median(list1, list2, size):
    merged_list = sorted(list1 + list2)
    return merged_list[size//2]


# Driver Code

list1 = [1, 12, 15, 26, 38]
list2 = [2, 13, 17, 30, 45]
size = 5

# Checking the result
assert get_median(list1, list2, size) == 16.0
print("All tests passed!")
```

To test the function, you can run the program and it will print "All tests passed!" if the assert statement passes, indicating that the median of the two lists is 16.0. Otherwise, an error message will be displayed, indicating that the assert statement failed.

Note: The function `get_median` takes three parameters: `list1`, `list2`, and `size`. It concatenates the two lists and sorts the result in ascending order. Then, it returns the median value of the merged list, which is the value at the index `size//2`.

In the provided example, `list1` is `[1, 12, 15, 26, 38]` and