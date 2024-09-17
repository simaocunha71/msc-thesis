def max_sub_array_sum_repeated(arr, k, n):
    if (k <= 0 or n <= 0):
        return -1
    if (n == 0):
        return 0

    max_sum = arr[0]
    curr_sum = arr[0]
    for i in range(1, len(arr)):
        curr_sum = max(arr[i], curr_sum + arr[i])
        max_sum = max(curr_sum, max_sum)

    max_sum *= k
    if (k > 1):
        curr_sum = 0
        for i in range(len(arr)):
            curr_sum = max(arr[i], curr_sum + arr[i])
            max_sum = max(curr_sum, max_sum)
    return max_sum