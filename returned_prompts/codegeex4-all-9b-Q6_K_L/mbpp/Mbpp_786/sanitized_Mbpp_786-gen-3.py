def right_insertion(arr, val):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= val:
            left = mid + 1
        else:
            right = mid
    return left