
    def minSubArraySum(nums):
        s, res = 0, float('inf')
        for i in nums:
            s += i
            if s < res:
                res = s
            if s < 0:
                s = 0
        return res





# Time: O(n)
# Space: O(1)


```

```
def minSubArraySum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    s, res = 0, float('inf')
    for i in nums:
        s += i
        if s < res:
            res = s
        if s < 0:
            s = 0
    return res
```

```

```

```

```

```

```

```
```