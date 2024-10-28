def max_sum(arr):
    n = len(arr)
    inc = [0]*n
    dec = [0]*n

    inc[0] = arr[0]
    dec[n-1] = arr[n-1]

    for i in range(1, n):
        if arr[i] > arr[i-1]:
            inc[i] = inc[i-1] + arr[i]
        else:
            inc[i] = arr[i]

    for i in range(n-2, -1, -1):
        if arr[i] > arr[i+1]:
            dec[i] = dec[i+1] + arr[i]
        else:
            dec[i] = arr[i]

    max_bitonic = max(inc[i] + dec[i] - arr[i] for i in range(n))

    return max_bitonic