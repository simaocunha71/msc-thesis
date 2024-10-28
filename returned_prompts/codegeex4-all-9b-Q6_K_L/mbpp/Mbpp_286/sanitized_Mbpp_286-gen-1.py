def max_sub_array_sum_repeated(arr, k, n):
    max_sum = float('-inf')
    current_sum = 0

    for i in range(n * k):
        current_sum += arr[i % n]
        if current_sum < 0:
            current_sum = 0
        max_sum = max(max_sum, current_sum)

    return max_sum