def max_product(arr):
    n = len(arr)

    if n < 1:
        return 0

    max_end = [0] * n
    min_end = [0] * n

    max_end[0] = min_end[0] = arr[0]

    for i in range(1, n):
        if arr[i] > 0:
            max_end[i] = max(arr[i], max_end[i-1]*arr[i])
            min_end[i] = min(arr[i], min_end[i-1]*arr[i])
        else:
            max_end[i] = max(arr[i], min_end[i-1]*arr[i])
            min_end[i] = min(arr[i], max_end[i-1]*arr[i])

    return max(max_end)