def max_Product(arr):
    n = len(arr)
    arr.sort()
    if (arr[0] * arr[1]) > (arr[n - 1] * arr[n - 2]):
        return (arr[0], arr[1])
    else:
        return (arr[n - 1], arr[n - 2])