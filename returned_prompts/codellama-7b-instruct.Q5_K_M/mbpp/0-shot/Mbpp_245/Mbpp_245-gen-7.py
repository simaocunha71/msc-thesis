def max_sum(arr):
    if len(arr) == 0:
        return 0

    max_sum_inc = arr[0]
    max_sum_dec = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            max_sum_inc = max(max_sum_inc + arr[i], arr[i])
        else:
            max_sum_dec = max(max_sum_dec + arr[i], arr[i])

    return max(max_sum_inc, max_sum_dec)
