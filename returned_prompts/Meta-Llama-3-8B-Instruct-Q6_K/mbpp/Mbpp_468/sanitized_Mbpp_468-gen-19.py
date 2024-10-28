def max_product(nums):
    if not nums:
        return 0

    dp = [num for num in nums]
    max_product = dp[0]
    for i in range(1, len(nums)):
        if dp[i] < 0:
            dp[i] = max(dp[i], dp[i-1] * dp[i])
        else:
            dp[i] = max(dp[i], dp[i-1] * dp[i])
        max_product = max(max_product, dp[i])
    return max_product