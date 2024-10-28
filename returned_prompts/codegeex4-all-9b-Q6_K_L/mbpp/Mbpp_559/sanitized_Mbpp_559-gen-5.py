def max_sub_array_sum(arr, n):
    current_sum = max_sum = arr[0]
    for i in range(1, n):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    return max_sum