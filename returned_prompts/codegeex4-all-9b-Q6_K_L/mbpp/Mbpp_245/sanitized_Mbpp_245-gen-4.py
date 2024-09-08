def max_sum(arr):
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    max_sum_inc = [0] * n
    max_sum_dec = [0] * n
    max_sum_inc[0] = arr[0]
    max_sum_dec[n-1] = arr[n-1]
    for i in range(1, n):
        max_sum_inc[i] = max(max_sum_inc[i-1], arr[i])
        max_sum_dec[n-i-1] = max(max_sum_dec[n-i], arr[n-i-1])
    max_sum_bitonic = [0] * n
    for i in range(n):
        max_sum_bitonic[i] = max_sum_inc[i] + max_sum_dec[i] - arr[i]
    return max(max_sum_bitonic)