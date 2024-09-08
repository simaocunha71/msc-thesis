def max_sum_increasing_subseq(arr, n, i, k):
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = arr[0]
    max_sum = 0

    for j in range(1, i + 1):
        dp[j] = max(dp[j - 1], arr[j])

    for j in range(i + 1, k + 1):
        max_sum = max(max_sum, dp[j])

    return max_sum