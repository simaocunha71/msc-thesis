def max_sum_increasing_subseq(arr, i, k, j):
    dp = [0] * (i + 1)
    for num in arr[:i+1]:
        for j in range(i, -1, -1):
            if num > dp[j]:
                dp[j] = num
    for num in arr[i+1:]:
        if num > dp[j]:
            dp[j] = num
    return sum(dp)