def find_min_diff(arr,n):
    arr.sort()
    min_diff = arr[1] - arr[0]
    for i in range(1, n-1):
        for j in range(i+1, n):
            if arr[j] - arr[i] < min_diff:
                min_diff = arr[j] - arr[i]
    return min_diff