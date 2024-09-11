def max_sub_array_sum_repeated(arr, k, m):
    arr = arr * k
    max_sum = float('-inf')
    current_sum = 0
    for num in arr:
        current_sum += num
        if current_sum < 0:
            current_sum = 0
        else:
            max_sum = max(max_sum, current_sum)
    return max_sum