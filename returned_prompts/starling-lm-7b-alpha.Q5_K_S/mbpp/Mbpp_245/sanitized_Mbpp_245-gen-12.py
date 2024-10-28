def max_sum(nums: list) -> int:
    n = len(nums)
    dp = [0 for _ in range(n)]
    dp[0] = nums[0]
    for i in range(1, n):
        dp[i] = max(nums[i], dp[i-1] + nums[i])
    return dp[-1]