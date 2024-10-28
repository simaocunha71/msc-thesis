def last(arr, target):
    if not arr:
        return -1
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            if arr[mid] == target:
                if mid == len(arr) - 1 or arr[mid + 1] != target:
                    return mid
                right = mid - 1
            else:
                right = mid - 1
    return -1