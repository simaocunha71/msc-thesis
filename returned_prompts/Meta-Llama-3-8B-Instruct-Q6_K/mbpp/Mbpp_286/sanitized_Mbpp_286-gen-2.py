def max_sub_array_sum_repeated(arr, k, n):
    arr = arr * k
    max_sum = float('-inf')
    current_sum = 0
    for i in range(n):
        current_sum += arr[i]
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    return max_sum