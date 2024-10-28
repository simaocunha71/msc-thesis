def find_first_occurrence(arr, target):
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] == target:
            high = mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return low