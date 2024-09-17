def max_sum(nums):
    n = len(nums)
    dp = [[0 for _ in range(n)] for _ in range(2)]
    for i in range(n):
        dp[i % 2][i] = nums[i]
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                dp[i % 2][j] = max(dp[(i + 1) % 2][j] + nums[j], dp[i % 2][j - 1])
            else:
                dp[i % 2][j] = max(dp[i % 2][j - 1], dp[(i + 1) % 2][j])
    return dp[n % 2][-1]