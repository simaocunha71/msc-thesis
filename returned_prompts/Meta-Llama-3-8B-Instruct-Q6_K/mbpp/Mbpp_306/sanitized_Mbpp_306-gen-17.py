def max_sum_increasing_subseq(arr, i, k, target):
    dp = [0] * (i + 1)
    for j in range(i + 1):
        dp[j] = max(dp[j - 1], arr[j] if j > 0 else 0)
    
    for j in range(i + 1, k + 1):
        dp[j] = max(dp[j - 1], dp[j - 1] + arr[j] if arr[j] > dp[j - 1] else 0)
    
    return dp[k]