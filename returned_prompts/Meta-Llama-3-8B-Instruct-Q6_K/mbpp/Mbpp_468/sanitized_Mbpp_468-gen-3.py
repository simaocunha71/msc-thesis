def max_product(nums):
    if not nums:
        return 0

    dp = [1] * len(nums)
    max_product = 1

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] * nums[i])
        max_product = max(max_product, dp[i])

    return max_product