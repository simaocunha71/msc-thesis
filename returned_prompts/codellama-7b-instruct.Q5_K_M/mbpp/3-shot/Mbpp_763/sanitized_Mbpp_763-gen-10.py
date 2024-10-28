def find_min_diff(arr,n):
    if n < 2:
        return -1
    min_diff = abs(arr[1] - arr[0])
    for i in range(1, n-1):
        for j in range(i+1, n):
            diff = abs(arr[j] - arr[i])
            if diff < min_diff:
                min_diff = diff
    return min_diff