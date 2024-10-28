def max_sum_increasing_subseq(arr, k, i, n):
    dp = [0] * (n + 1)
    dp[i] = arr[i]
    for j in range(i + 1, n + 1):
        dp[j] = max(dp[j], dp[i] + arr[j])
        if j == k:
            return dp[k]
    return -1