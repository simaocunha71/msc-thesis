def max_sub_array_sum_repeated(arr, k, n):
    max_sum = float('-inf')
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]
    for i in range(n):
        for j in range(i, n):
            sub_array_sum = prefix_sum[j + 1] - prefix_sum[i]
            for _ in range(k - 1):
                sub_array_sum += prefix_sum[j + 1] - prefix_sum[i]
            max_sum = max(max_sum, sub_array_sum)
    return max_sum