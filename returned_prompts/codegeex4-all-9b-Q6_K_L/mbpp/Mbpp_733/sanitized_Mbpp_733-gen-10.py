def find_first_occurrence(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid
            right = mid - 1  # Look for earlier occurrences
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result