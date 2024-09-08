def last(arr, element):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < element:
            left = mid + 1
        elif arr[mid] > element:
            right = mid - 1
        else:
            if mid == len(arr) - 1 or arr[mid + 1] != element:
                return mid
            else:
                left = mid + 1
    return -1