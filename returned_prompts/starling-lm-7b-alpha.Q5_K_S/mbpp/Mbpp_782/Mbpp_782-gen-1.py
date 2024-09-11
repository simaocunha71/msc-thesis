"""
def odd_length_sum(nums):
    n = len(nums)
    res = 0
    for i in range(1<<n):
        curr = 0
        for j in range(n):
            if (i&(1<<j)) != 0:
                curr += nums[j]
        res += curr if curr%2 else -curr
    return res

print(odd_length_sum([1,2,4]))  # 14
"""

def odd_length_sum(nums):
    n = len(nums)
    res = 0
    for mask in range(1<<n):
        curr = 0
        for j in range(n):
            if (mask & (1 << j)) != 0:
                curr += nums[j]
        res += curr if curr%2 else -curr
    return res

print(odd_length_sum([1,2,4]))  # 14





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