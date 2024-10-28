def max_Product(arr):
    arr.sort()
    n = len(arr)
    return (arr[n-1], arr[n-2]) if arr[0]*arr[1] < arr[n-1]*arr[n-2] else (arr[0], arr[1])