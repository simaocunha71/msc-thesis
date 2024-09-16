def left_insertion(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            right = mid - 1
        elif arr[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return left