The problem can be solved using dynamic programming where we store the result of each sub problem so that we can use it in future.

Here is the python code:

```python
def get_max_sum(n):
    dp = [0]*(n+1)
    for i in range(1, n+1):
        dp[i] = max(dp[i//2]+dp[i//3]+dp[i//4]+dp[i//5], i)
    return dp[n]
print(get_max_sum(60))
```

In the above code, we initialize a list `dp` with zeroes for storing the maximum sum for each number up to `n`. Then we iterate from 1 to `n` and for each `i`, we calculate the maximum sum as per the given equation. Finally, we return `dp[n]` which is the maximum sum for `n`.
"""

assert get_max_sum(60) == 106
```
"""
