def max_sum(nums):
    n = len(nums)

    # Initialize the table
    dp = [0] * (n + 1)
    for i in range(n):
        dp[i] = nums[i]

    # Dynamic programming
    for i in range(2, n + 1):
        for j in range(i - 2, -1, -1):
            dp[j] = max(dp[j], dp[j + 1])

    # Find the maximum
    return max(dp)