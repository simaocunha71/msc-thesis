def max_sum_increasing_subseq(arr, n, k, i):
    dp = [0]*n
    dp[i] = arr[i]
    for j in range(i+1, n):
        if arr[j] > arr[i]:
            dp[j] = max(dp[j], dp[i]+arr[j])
            i = j
    return dp[k-1]+arr[k]