def max_sub_array_sum(arr, size):
    max_sum = float('-inf')
    current_sum = 0
    for i in range(size):
        current_sum += arr[i]
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    return max_sum