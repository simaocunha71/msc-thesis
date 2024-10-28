def find_min_diff(arr):
    arr = sorted(arr)
    min_diff = float('inf')
    for i in range(1, len(arr)):
        min_diff = min(min_diff, arr[i] - arr[i-1])
    return min_diff