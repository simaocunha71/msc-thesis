def last(arr: list, item: int) -> int:
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == item:
            if mid == len(arr) - 1 or arr[mid + 1] != item:
                return mid
            else:
                left = mid + 1
        elif arr[mid] < item:
            left = mid + 1
        else:
            right = mid - 1
    return -1