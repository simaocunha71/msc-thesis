def find_first_occurrence(arr, num):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < num:
            low = mid + 1
        elif arr[mid] > num:
            high = mid - 1
        else:
            if mid == 0 or arr[mid - 1] < num:
                return mid
            high = mid - 1
    return -1