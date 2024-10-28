```python
def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    n = len(nums)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + nums[i - 1]
    min_sum = float('inf')
    for i in range(1, n + 1):
        for j in range(i):
            min_sum = min(min_sum, dp[i] - dp[j])
    return min_sum
```
