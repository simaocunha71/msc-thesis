def max_sum(nums):
    """
    Complexity: O(n)
    """
    dp = [0] * len(nums)
    for i in range(len(nums)):
        dp[i] = nums[i]
    for i in range(1, len(nums)):
        dp[i] = max(nums[i] + dp[i-1], dp[i])
    return dp[-1]