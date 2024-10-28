def get_median(arr1, arr2, n):
    if n <= 0:
        return None
    if n == 1:
        return (arr1[0] + arr2[0]) / 2
    mid1 = arr1[n // 2]
    mid2 = arr2[n // 2]
    if mid1 == mid2:
        return mid1
    elif mid1 < mid2:
        return get_median(arr1[n // 2:], arr2[:n // 2 + 1], n - n // 2)
    else:
        return get_median(arr1[:n // 2 + 1], arr2[n // 2:], n - n // 2)