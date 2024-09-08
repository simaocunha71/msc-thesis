def right_insertion(arr, val):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= val:
            left = mid + 1
        else:
            right = mid
    return left