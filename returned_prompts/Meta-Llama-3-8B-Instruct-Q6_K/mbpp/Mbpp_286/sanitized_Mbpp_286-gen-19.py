def max_sub_array_sum_repeated(arr, k, n):
    total_sum = sum(arr)
    max_sum = float('-inf')
    for i in range(n):
        sub_sum = sum(arr[i:i+n])
        max_sum = max(max_sum, sub_sum)
    return max_sum + (total_sum - max_sum) * k