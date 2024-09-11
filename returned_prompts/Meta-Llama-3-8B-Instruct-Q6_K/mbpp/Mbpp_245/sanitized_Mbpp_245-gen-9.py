def max_sum(arr):
    n = len(arr)
    max_sum = [0] * n
    max_sum[0] = arr[0]
    for i in range(1, n):
        max_sum[i] = max(max_sum[i-1], arr[i] + max_sum[i-2])
    return max_sum[-1]  # return the last element of max_sum array