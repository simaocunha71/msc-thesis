def last(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            if mid == len(arr) - 1 or arr[mid + 1] != x:
                return mid
            left = mid + 1
        else:
            right = mid - 1
    return -1