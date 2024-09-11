```
def max_product(nums):
    cur_max, cur_min, res = float('-inf'), float('inf'), 0
    for num in nums:
        cur_max, cur_min = max(num, cur_max * num), min(num, cur_min * num)
        res = max(res, cur_max * cur_min)
    return res
```

Explanation:
The key point of this problem is to find the increasing subsequence in the array and calculate the product of its numbers. In fact, we can only care about the maximum and minimum values of the current increasing subsequence, as the other values will not affect the maximum product. Thus, we maintain the maximum and minimum values of the current increasing subsequence, and for each new number, we update them to the maximum and minimum of the current number and the product of the current increasing subsequence. Finally, we return the product of the maximum and minimum values.

The time complexity of this method is O(n), and the space complexity is O(1).

This method is very efficient and can be used directly without the need for additional space.

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```
