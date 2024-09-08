def max_sub_array_sum(nums, k):
    max_sum = float('-inf')
    dp = [0] * k
    for i in range(len(nums)):
        dp[i % k] = max(dp[i % k] + nums[i], nums[i])
        max_sum = max(max_sum, dp[i % k])
    return max_sum