def find_first_occurrence(arr, val):
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == val:
            if mid == 0 or arr[mid - 1] < val:
                return mid
            else:
                hi = mid - 1
        elif val < arr[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1