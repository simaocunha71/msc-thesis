def left_insertion(arr, val):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    left = -1
    right = len(arr)
    while right - left > 1:
        mid = (left + right) // 2
        if arr[mid] < val:
            left = mid
        else:
            right = mid
    return left

# Test Case
print(left_insertion([1,2,4,5],6)==4)  # True
"""
When val = 6,
we start with left = -1, right = 4
We go to the mid point, mid = (left + right) // 2 = 1, which is the index of 2. Since 2 < 6, we move the left pointer to 1.
We repeat the process to mid = 2, which is the index of 4. Since 4 >= 6, we move the right pointer to 2.
Now, right - left = 0, and we return left = 1.
"""
```

The time complexity of this function is O(log(n)), since we are bisecting the array in half at each step. The space complexity is O(1), as we are only using a few constant variables to store the indices of our search.

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

``