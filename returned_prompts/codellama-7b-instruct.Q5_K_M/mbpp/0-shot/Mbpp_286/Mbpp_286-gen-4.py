def max_sub_array_sum_repeated(arr, k, max_repeats):
    # Find the largest sum of a contiguous array in the modified array which is formed by repeating the given array k times.
    # https://www.geeksforgeeks.org/find-largest-sum-contiguous-array-repeating-given-array/
    # modified from geeksforgeeks
    # modified to take in a max_repeats
    n = len(arr)
    dp = [0]*(n*k)
    for i in range(n):
        dp[i] = arr[i]

    for i in range(1, n*k):
        for j in range(i, max(0, i-k+1), -1):
            dp[i] = max(dp[i], dp[j] + arr[i-j])

    return max(dp)
