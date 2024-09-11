```python
def multiple_to_single(nums):
    """
    Join a list of multiple integers into a single integer.

    :type nums: List[int]
    :rtype: int
    """
    return int(''.join(map(str, nums)))
```

To use this function, you can call it with a list of integers as an argument, like this:

```python
result = multiple_to_single([11, 33, 50])
print(result)  # Output: 113350
```

The function will join the integers in the list into a single integer by converting each integer to a