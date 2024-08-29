def find_min_diff(arr,n):
    arr = sorted(arr)
    min_diff = float('inf')
    for i in range(n-1):
        diff = abs(arr[i+1] - arr[i])
        min_diff = min(min_diff, diff)
    return min_diff