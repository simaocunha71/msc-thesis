def max_sum_increasing_subseq(arr, n, i, k):
    dp = [0]*n
    index = [-1]*n
    max_sum = 0
    max_index = -1

    for j in range(n):
        for l in range(j):
            if arr[l] < arr[j] and dp[l] > dp[j]:
                dp[j] = dp[l]
                index[j] = l
        dp[j] += arr[j]
        if dp[j] > max_sum:
            max_sum = dp[j]
            max_index = j

    if k >= i:
        return max_sum

    prefix_sum = [0]
    for p in range(i):
        prefix_sum.append(prefix_sum[-1] + arr[p])

    max_sum_prefix_k = prefix_sum[k]
    while max_index >= 0:
        if index[max_index] >= i:
            max_sum_prefix_k = max(max_sum_prefix_k, prefix_sum[index[max_index]+1] + arr[max_index])
        max_index = index[max_index]

    return max_sum_prefix_k