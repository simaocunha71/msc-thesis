def find_first_occurrence(arr, num):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == num:
            if mid == 0 or arr[mid - 1] != num:
                return mid
            else:
                right = mid - 1
        elif arr[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return -1