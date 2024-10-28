def max_Product(arr):
    arr.sort()
    if arr[-1] > 0:
        return arr[-1], arr[-2]
    else:
        return arr[0], arr[1]