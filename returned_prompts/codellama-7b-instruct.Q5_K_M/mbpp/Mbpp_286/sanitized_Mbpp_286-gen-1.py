def max_sub_array_sum_repeated(arr, k, n):
    # Write your code here
    # Initialize the variables
    dp = [0] * (k + 1)
    res = 0
    for i in range(n):
        for j in range(1, k + 1):
            dp[j] = max(dp[j], dp[j - 1] + arr[i])
        res = max(res, dp[k])
    return res