def max_sum(arr):
    n = len(arr)
    inc = [0] * n
    dec = [0] * n
    inc[0] = arr[0]
    dec[n-1] = arr[n-1]
    for i in range(1, n):
        inc[i] = max(inc[i-1], arr[i])
    for i in range(n-2, -1, -1):
        dec[i] = max(dec[i+1], arr[i])
    return sum(inc) + sum(dec) - arr[0] - arr[n-1]