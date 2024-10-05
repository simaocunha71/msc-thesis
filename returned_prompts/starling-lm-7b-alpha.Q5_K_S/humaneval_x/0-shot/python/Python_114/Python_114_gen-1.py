
def minSubArraySum(nums):
    cur_sum = min_sum = nums[0]
    for i in nums[1:]:
        cur_sum = min(i, cur_sum + i)
        min_sum = min(min_sum, cur_sum)
    return min_sum

# Time: O(n)
# Space: O(1)

def minSubArraySum2(nums):
    min_sum = float("inf")
    for i in range(len(nums)):
        cur_sum = 0
        for j in range(i, len(nums)):
            cur_sum += nums[j]
            min_sum = min(min_sum, cur_sum)
    return min_sum

# Time: O(n^2)
# Space: O(1)



















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