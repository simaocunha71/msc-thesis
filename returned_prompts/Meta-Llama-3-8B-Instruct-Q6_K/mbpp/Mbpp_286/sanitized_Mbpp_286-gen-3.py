def max_sub_array_sum_repeated(arr, k, n):
    max_sum = float('-inf')
    for i in range(n):
        for j in range(i, n):
            total_sum = sum(arr[i:j+1])
            if total_sum > max_sum:
                max_sum = total_sum
    return max_sum * k