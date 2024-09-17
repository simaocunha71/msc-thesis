def max_sum_increasing_subseq(arr, i, k, j):
    dp = [0] * len(arr)
    max_sum = 0
    for idx in range(i+1):
        dp[idx] = arr[idx]
    for idx in range(i+1, j):
        dp[idx] = max(dp[idx-1], arr[idx])
    for idx in range(j, k):
        if arr[idx] > dp[idx-1]:
            dp[idx] = arr[idx] + dp[idx-1]
        else:
            dp[idx] = dp[idx-1]
    for idx in range(k, len(arr)):
        if arr[idx] > dp[idx-1]:
            dp[idx] = arr[idx] + dp[idx-1]
        else:
            dp[idx] = dp[idx-1]
    return max(dp)