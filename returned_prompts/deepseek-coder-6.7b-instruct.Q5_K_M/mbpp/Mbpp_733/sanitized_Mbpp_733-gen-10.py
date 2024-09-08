def find_first_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    first_occurrence = -1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            first_occurrence = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return first_occurrence