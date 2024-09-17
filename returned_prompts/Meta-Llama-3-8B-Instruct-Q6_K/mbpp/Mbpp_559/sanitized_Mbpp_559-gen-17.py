def max_sub_array_sum(arr):
    max_sum = float('-inf')
    current_sum = 0
    for i in range(len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    return max_sum