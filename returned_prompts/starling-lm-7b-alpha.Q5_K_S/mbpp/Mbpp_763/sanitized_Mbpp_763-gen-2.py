def find_min_diff(arr,n):
    arr.sort()
    min_diff = float('inf')
    for i in range(len(arr)-1):
        diff = abs(arr[i] - arr[i+1])
        min_diff = min(min_diff,diff)
    return min_diff