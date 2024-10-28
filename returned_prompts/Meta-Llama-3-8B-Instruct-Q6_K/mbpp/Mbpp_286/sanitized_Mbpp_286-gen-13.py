def max_sub_array_sum_repeated(arr, k, n):
    total_sum = sum(arr)
    max_sum = float('-inf')
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            window_sum = sum(arr[i:j+1])
            max_sum = max(max_sum, window_sum)
    return max_sum * k + (total_sum - max_sum) * n