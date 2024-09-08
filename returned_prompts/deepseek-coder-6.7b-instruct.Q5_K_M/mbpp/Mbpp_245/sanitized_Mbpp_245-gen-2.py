def max_sum(arr):
    n = len(arr)
    inc = [0]*n
    dec = [0]*n

    # calculating increasing sum
    inc[0] = arr[0]
    for i in range(1, n):
        inc[i] = max(inc[i-1], arr[i]) if arr[i] > arr[i-1] else arr[i]

    # calculating decreasing sum
    dec[-1] = arr[-1]
    for i in range(n-2, -1, -1):
        dec[i] = max(dec[i+1], arr[i]) if arr[i] > arr[i+1] else arr[i]

    # calculating maximum sum of bitonic subsequences
    bitonic_sum = [0]*n
    for i in range(n):
        bitonic_sum[i] = inc[i] + dec[i] - arr[i] if inc[i] > dec[i] else inc[i] if inc[i] > arr[i] else dec[i] if dec[i] > arr[i] else arr[i]

    return max(bitonic_sum)