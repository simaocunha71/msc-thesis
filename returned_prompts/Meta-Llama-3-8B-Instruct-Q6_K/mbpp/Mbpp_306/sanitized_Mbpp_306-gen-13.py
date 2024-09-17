def max_sum_increasing_subseq(arr, i, k, j):
    dp = [0] * len(arr)
    dp[0] = arr[0]
    for idx in range(1, i+1):
        dp[idx] = max(dp[idx-1], arr[idx])
    max_sum = dp[i]
    for idx in range(i+1, k+1):
        dp[idx] = max(dp[idx-1], dp[idx-1] + arr[idx])
    max_sum += dp[k]
    for idx in range(k+1, len(arr)):
        dp[idx] = max(dp[idx-1], dp[idx-1] + arr[idx])
    return max(dp[j], max_sum)