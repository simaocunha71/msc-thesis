def max_sum(nums):
    n = len(nums)
    dp = [0] * n
    for i in range(n):
        dp[i] = nums[i]
    for i in range(1, n):
        for j in range(n - i):
            dp[j] += max(dp[j], dp[j + i])
    return dp[0]