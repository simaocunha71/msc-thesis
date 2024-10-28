def max_sub_array_sum(arr, n):
    max_sum = float('-inf')
    window_sum = 0
    for i in range(n):
        window_sum += arr[i]
        max_sum = max(max_sum, window_sum)
        if window_sum < 0:
            window_sum = 0
    return max_sum