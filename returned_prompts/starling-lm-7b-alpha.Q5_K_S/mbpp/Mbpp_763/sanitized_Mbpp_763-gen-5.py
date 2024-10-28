def find_min_diff(arr, num):
    arr = sorted(arr)
    min_diff = float('inf')
    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] < min_diff:
            min_diff = arr[i+1] - arr[i]
    return min_diff
arr = [1,5,3,19,18,25]
num = 6