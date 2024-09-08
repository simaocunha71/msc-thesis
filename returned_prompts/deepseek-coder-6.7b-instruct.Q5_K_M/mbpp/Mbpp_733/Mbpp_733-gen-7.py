def find_first_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            result = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result

print(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5))

"""
