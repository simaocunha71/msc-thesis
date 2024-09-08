def right_insertion(arr, n):
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if n < arr[mid]:
            high = mid
        else:
            low = mid + 1
    return low