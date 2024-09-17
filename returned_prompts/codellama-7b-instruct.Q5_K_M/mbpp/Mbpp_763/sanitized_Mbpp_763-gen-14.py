def find_min_diff(arr, n):
    diff = arr[1] - arr[0]
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            temp_diff = arr[j] - arr[i]
            if temp_diff < diff:
                diff = temp_diff
    return diff