def last(arr, elem):
    n = len(arr)
    if elem not in arr:
        return -1
    first = 0
    last = n-1
    while first < last:
        mid = (first + last)//2
        if arr[mid] > elem:
            last = mid - 1
        else:
            first = mid + 1
    return last