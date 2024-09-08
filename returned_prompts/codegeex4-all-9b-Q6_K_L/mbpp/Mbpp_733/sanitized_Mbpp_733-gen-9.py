def find_first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            if mid == 0 or arr[mid - 1] != target:
                return mid
            else:
                right = mid - 1
    return -1