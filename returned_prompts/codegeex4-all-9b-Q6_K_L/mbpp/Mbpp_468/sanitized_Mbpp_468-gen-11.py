def max_product(nums):
    n = len(nums)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            dp[i] = max(dp[i], dp[j]*nums[i])
    return max(dp)