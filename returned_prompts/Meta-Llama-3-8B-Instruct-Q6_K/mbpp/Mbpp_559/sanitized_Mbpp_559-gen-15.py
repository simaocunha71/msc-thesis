def max_sub_array_sum(arr, n):
    max_current = max_global = arr[0]
    for i in range(1, n):
        max_current = max(arr[i], max_current + arr[i])
        if max_current > max_global:
            max_global = max_current
    return max_global