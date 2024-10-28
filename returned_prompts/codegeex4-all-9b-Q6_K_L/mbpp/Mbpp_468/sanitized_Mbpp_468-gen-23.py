def max_product(nums: list) -> int:
    dp = [0]*len(nums)
    dp[0] = nums[0]
    max_product = dp[0]
    for i in range(1, len(nums)):
        dp[i] = nums[i]
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] * nums[i])
        max_product = max(max_product, dp[i])
    return max_product