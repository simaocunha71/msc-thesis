def max_product(nums):
    dp = [num for num in nums]
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] * nums[i])
    return max(dp) if dp else 0