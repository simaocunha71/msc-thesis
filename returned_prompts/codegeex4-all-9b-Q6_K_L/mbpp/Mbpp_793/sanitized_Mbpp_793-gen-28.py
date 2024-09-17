def last(arr, n):
    low = 0
    high = len(arr) - 1
    last_pos = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == n:
            last_pos = mid
            low = mid + 1
        elif arr[mid] > n:
            high = mid - 1
        else:
            low = mid + 1
    return last_pos