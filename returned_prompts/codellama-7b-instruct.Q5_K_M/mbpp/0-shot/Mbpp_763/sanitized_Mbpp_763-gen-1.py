def find_min_diff(arr):
    arr.sort()
    min_diff = sys.maxsize
    for i in range(len(arr)-1):
        min_diff = min(min_diff, arr[i+1]-arr[i])
    return min_diff