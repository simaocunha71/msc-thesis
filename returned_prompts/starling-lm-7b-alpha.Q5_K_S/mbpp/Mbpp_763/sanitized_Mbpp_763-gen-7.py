def find_min_diff(arr,k):
    arr.sort()
    min_diff = float("inf")
    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] < min_diff:
            min_diff = arr[i+1] - arr[i]
    return min_diff