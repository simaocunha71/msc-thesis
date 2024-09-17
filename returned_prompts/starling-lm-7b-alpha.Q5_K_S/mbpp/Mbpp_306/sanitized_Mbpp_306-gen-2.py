def max_sum_increasing_subseq(nums, i, k):
    n = len(nums)

    # DP table to store maximum sum of increasing subsequence until ith index
    dp = [0] * n
    for j in range(n):
        if j == 0 or nums[j] > nums[j-1]:
            dp[j] = nums[j]
        else:
            dp[j] = max(dp[j-1], nums[j])

    # Find maximum sum of increasing subsequence including kth element
    max_sum = 0
    for j in range(n):
        if j == i:
            continue
        elif nums[j] == k:
            max_sum = max(max_sum, dp[j] + k)
        elif nums[j] < k:
            max_sum = max(max_sum, dp[j])

    return max_sum