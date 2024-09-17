def max_sub_array_sum_repeated(arr, k, n):
    arr = arr * k
    max_sum = float('-inf')
    for i in range(len(arr)):
        window_sum = 0
        for j in range(i, len(arr)):
            window_sum += arr[j]
            max_sum = max(max_sum, window_sum)
    return max_sum