def get_max_sum(n):
    # Initialize the array with 0
    max_sum = [0] * (n + 1)

    # For each number, calculate the maximum sum
    for i in range(1, n + 1):
        if i % 2 == 0:
            max_sum[i] = max_sum[i // 2] + max_sum[i // 2] + 1
        elif i % 3 == 0:
            max_sum[i] = max_sum[i // 3] + max_sum[i // 3] + 1
        elif i % 4 == 0:
            max_sum[i] = max_sum[i // 4] + max_sum[i // 4] + 1
        elif i % 5 == 0:
            max_sum[i] = max_sum[i // 5] + max_sum[i // 5] + 1
        else:
            max_sum[i] = i

    return max_sum[n]