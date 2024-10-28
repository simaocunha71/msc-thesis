def find_min_diff(arr, n):
    if n < 2:
        return float('inf')
    
    arr.sort()
    min_diff = float('inf')
    
    for i in range(1, n):
        min_diff = min(min_diff, arr[i] - arr[i-1])
    
    return min_diff