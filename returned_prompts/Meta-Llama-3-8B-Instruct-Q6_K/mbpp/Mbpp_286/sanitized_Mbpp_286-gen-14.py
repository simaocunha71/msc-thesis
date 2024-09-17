def max_sub_array_sum_repeated(arr, k, n):
    repeated_arr = arr * k
    max_sum = float('-inf')
    for i in range(len(repeated_arr)):
        for j in range(i, len(repeated_arr)):
            window_sum = sum(repeated_arr[i:j+1])
            max_sum = max(max_sum, window_sum)
    return max_sum