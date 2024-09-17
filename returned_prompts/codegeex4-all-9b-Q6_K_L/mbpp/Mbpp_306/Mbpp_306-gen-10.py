def max_sum_increasing_subseq(nums, k, i, n):
    dp = [0] * (n + 1)
    dp[0] = nums[i]
    for j in range(i + 1, k):
        dp[j] = max(dp[j - 1], nums[j])
    return dp[k - 1] + nums[k - 1]

