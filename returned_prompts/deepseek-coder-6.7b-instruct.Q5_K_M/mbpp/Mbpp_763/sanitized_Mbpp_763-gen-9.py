def find_min_diff(arr, n):
    # sort the array
    arr = sorted(arr)
    
    # initialize the minimum difference
    min_diff = float('inf')
    
    # find the minimum difference
    for i in range(1, n):
        diff = arr[i] - arr[i-1]
        min_diff = min(min_diff, diff)
    
    return min_diff