def find_min_diff(arr, n):
    arr.sort()
    min_diff = arr[1] - arr[0]
    for i in range(2, n):
        min_diff = min(min_diff, arr[i] - arr[i-1])
    return min_diff