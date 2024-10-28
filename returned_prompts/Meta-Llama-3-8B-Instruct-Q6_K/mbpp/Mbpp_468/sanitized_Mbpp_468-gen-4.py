def max_product(nums):
    n = len(nums)
    dp = [1] * n
    max_product = 0
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] * nums[i])
        max_product = max(max_product, dp[i])
    return max_product