def max_sub_array_sum_repeated(arr, k, window_size):
    def max_sub_array_sum(arr, window_size):
        max_sum = 0
        current_sum = sum(arr[:window_size])
        max_sum = current_sum
        for i in range(window_size, len(arr)):
            current_sum = current_sum - arr[i - window_size] + arr[i]
            max_sum = max(max_sum, current_sum)
        return max_sum
    
    if k == 1:
        return max_sub_array_sum(arr, window_size)
    
    repeated_arr = arr * k
    return max_sub_array_sum(repeated_arr, window_size)