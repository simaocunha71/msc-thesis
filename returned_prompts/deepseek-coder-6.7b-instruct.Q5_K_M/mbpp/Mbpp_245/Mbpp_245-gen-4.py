
def max_sum(arr):
    n = len(arr)

    if n < 3:
        return -1

    inc = [0]*n
    dec = [0]*n

    inc[0] = arr[0]
    dec[n-1] = arr[n-1]

    for i in range(1, n):
        inc[i] = max(inc[i-1], arr[i])

    for i in range(n-2, -1, -1):
        dec[i] = max(dec[i+1], arr[i])

    bitonic = [0]*n

    for i in range(n):
        bitonic[i] = inc[i] + dec[i] - arr[i]

    return max(bitonic)


