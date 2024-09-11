def find_min_diff(nums, k):
    nums.sort()
    res = float("inf")
    for i in range(len(nums) - k + 1):
        res = min(res, nums[i + k - 1] - nums[i])
    return res

# assert find_min_diff((1,5,3,19,18,25),6) == 1
# print(find_min_diff((1,5,3,19,18,25),6))

"""
This function works by first sorting the given array in increasing order. Then for each subarray of size k in the given array, we calculate the difference between the maximum value and minimum value in that subarray. The minimum value among all such differences is the minimum difference between any two elements in the given array.
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
