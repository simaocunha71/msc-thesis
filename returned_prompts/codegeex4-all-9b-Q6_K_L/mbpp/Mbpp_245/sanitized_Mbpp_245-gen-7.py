def max_sum(arr):
    n = len(arr)
    if n == 0:
        return 0

    # Initialize the maximum sum array
    max_sum_arr = [0] * n

    # Initialize the maximum sum of increasing subsequence array
    max_sum_inc = [0] * n

    # Initialize the maximum sum of decreasing subsequence array
    max_sum_dec = [0] * n

    # Calculate the maximum sum of increasing subsequence
    max_sum_inc[0] = arr[0]
    for i in range(1, n):
        max_sum_inc[i] = max(max_sum_inc[i-1], arr[i])

    # Calculate the maximum sum of decreasing subsequence
    max_sum_dec[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        max_sum_dec[i] = max(max_sum_dec[i+1], arr[i])

    # Calculate the maximum sum of bitonic subsequence
    max_sum_arr[0] = max_sum_inc[0] + max_sum_dec[0]
    for i in range(1, n):
        max_sum_arr[i] = max(max_sum_arr[i-1], max_sum_inc[i] + max_sum_dec[i])

    return max_sum_arr[n-1]