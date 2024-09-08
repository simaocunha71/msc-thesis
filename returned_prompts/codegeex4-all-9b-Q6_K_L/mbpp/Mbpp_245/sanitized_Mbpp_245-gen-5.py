def max_sum(arr):
    if not arr:
        return 0
    n = len(arr)
    inc = [0] * n
    dec = [0] * n
    inc[0] = arr[0]
    for i in range(1, n):
        inc[i] = max(inc[i-1], arr[i])
        dec[i] = max(dec[i-1], inc[i-1] + arr[i])
    return dec[-1]