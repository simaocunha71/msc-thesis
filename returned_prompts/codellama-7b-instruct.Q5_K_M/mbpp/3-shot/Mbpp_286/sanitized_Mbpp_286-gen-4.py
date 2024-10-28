def max_sub_array_sum_repeated(arr, n, k):
    curr_sum = 0
    max_sum = 0
    for i in range(n):
        curr_sum += arr[i]
        if i >= k:
            curr_sum -= arr[i-k]
        if curr_sum > max_sum:
            max_sum = curr_sum
    return max_sum