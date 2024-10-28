def right_insertion(arr, num):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == num:
            left = mid + 1
        elif arr[mid] > num:
            right = mid - 1
        else:
            left = mid + 1
    return left