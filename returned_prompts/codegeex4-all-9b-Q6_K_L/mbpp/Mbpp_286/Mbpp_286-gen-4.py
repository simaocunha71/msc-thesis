def max_sub_array_sum_repeated(arr, n, k):
    sum = 0
    for i in range(n):
        sum += arr[i]
    max_sum = sum
    for i in range(1, k):
        sum = sum + arr[i*n] - arr[i*n-n]
        if sum > max_sum:
            max_sum = sum
    return max_sum

