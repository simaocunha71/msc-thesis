def max_product(nums):
    if not nums:
        return 0

    dp = [num for num in nums]
    max_dp = [num for num in nums]

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] * nums[i])
                max_dp[i] = max(max_dp[i], max_dp[j] * nums[i])

    return max(max_dp)