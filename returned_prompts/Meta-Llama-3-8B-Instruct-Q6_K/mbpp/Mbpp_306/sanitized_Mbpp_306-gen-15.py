def max_sum_increasing_subseq(arr, i, k, t):
    dp = [0] * (i + 1)
    for j in range(i):
        if arr[j] < arr[j + 1]:
            dp[j + 1] = max(dp[j], dp[j] + arr[j + 1])
        else:
            dp[j + 1] = dp[j]
    for j in range(i, k):
        if arr[j] > arr[j - 1]:
            dp[j] = max(dp[j - 1], dp[j - 1] + arr[j])
        else:
            dp[j] = dp[j - 1]
    return dp[k - 1] + t