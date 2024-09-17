def max_sum(arr):
    if len(arr) <= 2:
        return max(arr)

    max_left = [0] * len(arr)
    max_right = [0] * len(arr)

    max_left[0] = arr[0]
    max_right[-1] = arr[-1]

    for i in range(1, len(arr)):
        max_left[i] = max(max_left[i-1], arr[i])
        for j in range(i-2, -1, -1):
            max_left[i] = max(max_left[i], arr[j] + max_left[j])

    for i in range(len(arr) - 2, -1, -1):
        max_right[i] = max(max_right[i+1], arr[i])
        for j in range(i+2, len(arr)):
            max_right[i] = max(max_right[i], arr[j] + max_right[j])

    return max(max_left[-1], max_right[0])