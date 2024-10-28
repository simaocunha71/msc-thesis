def max_sum(arr):
    n = len(arr)
    inc = [1]*n
    dec = [1]*n
    for i in range(1, n):
        if arr[i-1] < arr[i]:
            inc[i] = inc[i-1] + 1
        if i > 0 and arr[i-1] > arr[i]:
            dec[i] = dec[i-1] + 1
    max_sum = 0
    for i in range(n):
        max_sum = max(max_sum, inc[i] + dec[i] - 1)
    return max_sum