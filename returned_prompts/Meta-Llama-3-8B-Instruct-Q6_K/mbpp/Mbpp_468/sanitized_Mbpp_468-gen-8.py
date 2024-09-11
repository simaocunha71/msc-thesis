def max_product(nums):
    if not nums:
        return 0

    dp = [0] * len(nums)
    dp[0] = nums[0]

    max_product = dp[0]
    for i in range(1, len(nums)):
        dp[i] = max(nums[i], dp[i-1] * nums[i])
        max_product = max(max_product, dp[i])

    return max_product