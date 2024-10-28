def last(arr, element):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > element:
            high = mid - 1
        elif arr[mid] < element:
            low = mid + 1
        else:
            return mid
    return -1
