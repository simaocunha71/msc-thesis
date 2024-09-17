def max_sum_increasing_subseq(arr, i, k, m):
    dp = [0] * (i+1)
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + arr[i])
    for j in range(i+1, k+1):
        if arr[j-1] < arr[k]:
            dp[k] = max(dp[k], dp[j-1] + arr[k])
    return sum(dp)