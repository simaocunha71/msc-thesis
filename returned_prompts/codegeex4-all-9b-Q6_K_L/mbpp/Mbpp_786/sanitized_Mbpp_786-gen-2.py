def right_insertion(arr, val):
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < val:
            low = mid + 1
        else:
            high = mid
    return low