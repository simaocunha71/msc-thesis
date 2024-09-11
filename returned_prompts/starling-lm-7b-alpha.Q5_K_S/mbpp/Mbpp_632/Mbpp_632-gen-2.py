def move_zero(nums):
    zero_index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero_index] = nums[zero_index], nums[i]
            zero_index += 1
    return nums


# Testing
assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]


# Time Complexity: O(n)
# Space Complexity: O(1)


"""
Explanation:
1. Traverse the given array from left to right.
2. Whenever an element is found that is not zero, it is swapped with the element at the zero_index. This effectively moves the non-zero element to its correct position. The zero is now at the original position of the non-zero element.
3. The zero_index is then incremented by one, effectively moving the zero to the end of the array.
4. This process is repeated until all non-zero elements have been swapped to their correct positions.
5. The array is returned as the final result.
"""



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

```

```

```

```

```

```

```

```
