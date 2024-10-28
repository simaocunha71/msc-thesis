def max_sum(arr):
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    if n == 2:
        return max(arr[0], arr[1])
    max_sum_inc = max_sum_dec = 0
    for i in range(n):
        max_sum_inc = max(max_sum_inc, arr[i] + max_sum_dec)
        max_sum_dec = max(max_sum_dec, arr[n - i - 1] + max_sum_inc)
    return max(max_sum_inc, max_sum_dec)