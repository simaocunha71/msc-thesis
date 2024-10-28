def max_sub_array_sum_repeated(arr, k, n):
    # Initialize variables
    max_sum = float('-inf')
    current_sum = 0
    prefix_sum = [0] * (2 * n + 1)
    hash_map = {}

    # Calculate prefix sum
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]

    # Calculate prefix sum for k times
    for i in range(n, 2 * n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i - n]

    # Calculate maximum subarray sum
    for i in range(2 * n + 1):
        current_sum += prefix_sum[i]
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0

    # Return maximum subarray sum
    return max_sum