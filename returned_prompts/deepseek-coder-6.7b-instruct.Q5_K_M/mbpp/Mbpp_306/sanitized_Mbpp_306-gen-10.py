def max_sum_increasing_subseq(arr, n, k, i):
    if i > n or i < 0 or k > n or k < 0:
        return -1

    dp = [0]*n
    dp[i] = arr[i]
    max_sum = dp[i]

    for j in range(i+1, n):
        for x in range(i, j):
            if arr[j] > arr[x]:
                dp[j] = max(dp[j], dp[x]+arr[j])
        max_sum = max(max_sum, dp[j])

    return max_sum + arr[k]