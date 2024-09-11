def max_Product(nums):
    max1, max2 = float('-inf'), float('-inf')
    min1, min2 = float('inf'), float('inf')
    for i in nums:
        if i > max1:
            max2 = max1
            max1 = i
        elif i > max2:
            max2 = i
        if i < min1:
            min2 = min1
            min1 = i
        elif i < min2:
            min2 = i
    return (max1 * max2 if max1 * max2 > min1 * min2 else min1 * min2)

# Test
assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)





"""
Find the maximum product of two elements in an array of integers such that they are not the same.

If there are multiple pairs with the same maximum product, return any pair will do.

For example, given the array [3,4,2,5,1], return (4,5) as 4 * 5 = 20 and it's the maximum product.

For example, given the array [1,2,3,4,7,0,8,4], return (7,8) as 7 * 8 = 56 and it's the maximum product.
"""



"""
Time complexity: O(n)
Space complexity: O(1)
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

``