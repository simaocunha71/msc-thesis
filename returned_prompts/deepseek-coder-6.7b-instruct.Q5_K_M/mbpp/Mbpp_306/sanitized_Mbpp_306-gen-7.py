def max_sum_increasing_subseq(arr, n, k, i):
    if i >= n or i < 0 or k >= n or k < 0:
        return 0
    dp = [0]*n
    dp[i] = arr[i]
    max_sum = dp[i]
    for j in range(i+1, n):
        if arr[j] > arr[i]:
            dp[j] = max(dp[j], dp[i]+arr[j])
            max_sum = max(max_sum, dp[j])
    for j in range(i-1, -1, -1):
        if arr[j] < arr[i]:
            dp[j] = max(dp[j], dp[i]+arr[j])
            max_sum = max(max_sum, dp[j])
    max_sum += arr[k]
    return max_sum