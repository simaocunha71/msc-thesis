def find_min_diff(arr):
    arr = sorted(arr)
    min_diff = float('inf')
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i-1]
        if diff < min_diff:
            min_diff = diff
    return min_diff