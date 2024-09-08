def max_Product(arr):
    arr.sort()
    n = len(arr)
    # two highest numbers
    if (arr[0] * arr[1]) > (arr[n - 1] * arr[n - 2]):
        return (arr[0], arr[1])
    else:
        return (arr[n - 1], arr[n - 2])