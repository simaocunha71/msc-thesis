def left_insertion(array, value):
    lo = 0
    hi = len(array)
    while lo < hi:
        mid = (lo + hi) // 2
        if array[mid] < value:
            lo = mid + 1
        else:
            hi = mid
    return lo