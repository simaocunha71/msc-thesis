def last(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            if mid == len(arr) - 1 or arr[mid + 1] != target:
                return mid
            else:
                l = mid + 1
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1