def max_sub_array_sum_repeated(arr, k, n):
    total_sum = sum(arr)
    max_sum = float('-inf')
    for i in range(1 << n):
        temp_sum = 0
        for j in range(n):
            if (i & (1 << j)):
                temp_sum += arr[j]
        temp_sum *= k
        max_sum = max(max_sum, temp_sum)
    return max_sum + (total_sum - max_sum) if total_sum > max_sum else total_sum