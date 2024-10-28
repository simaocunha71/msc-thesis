def find_min_diff(arr, n):
    arr.sort()
    min_diff = sys.maxsize
    for i in range(n-1):
        min_diff = min(min_diff, abs(arr[i]-arr[i+1]))
    return min_diff