def left_insertion(arr, val):
    """
    Time: O(log n)
    Space: O(1)
    """
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
    return left

# Test Case
arr = [1, 2, 4, 5]
val = 6
print(left_insertion(arr, val))  # 4






# Time: O(log n)
# Space: O(1)


```

```
"""
Write a function to locate the left insertion point for a specified value in sorted order. 
assert left_insertion([1,2,4,5],6)==4
"""

# Time: O(log n)
# Space: O(1)
def left_insertion(arr, val):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
    return left
```
```

```python
"""
Write a function to locate the left insertion point for a specified value in sorted order. 
assert left_insertion([1,2,4,5],6)==4
"""

# Time: O(log n)
# Space: O(1)
def left_insertion(arr, val):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
    return left
```
```

```python
"""
Write a function to locate the left insertion point for a specified value in sorted order. 
assert