def max_sum(arr):
    max_sum = 0
    for i in range(len(arr)):
        max_sum = max(max_sum, arr[i])
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                max_sum = max(max_sum, arr[i] + arr[j])
    return max_sum