def max_sum(arr):
    if len(arr) == 0:
        return 0

    left_max = [0] * len(arr)
    right_max = [0] * len(arr)
    left_max[0] = arr[0]
    right_max[-1] = arr[-1]

    for i in range(1, len(arr)):
        left_max[i] = max(left_max[i - 1], arr[i])
        right_max[-(i + 1)] = max(right_max[-i], arr[-(i + 1)])

    max_sum_subsequences = left_max[len(arr) - 1]

    for i in range(1, len(arr)):
        max_sum_subsequences = max(max_sum_subsequences, left_max[i - 1] + right_max[i])

    return max_sum_subsequences