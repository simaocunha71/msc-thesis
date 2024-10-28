def find_first_occurrence(arr, num):
    left = 0
    right = len(arr) - 1
    index = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == num:
            index = mid
            right = mid - 1  # Continue searching in the left half
        elif arr[mid] < num:
            left = mid + 1
        else:
            right = mid - 1

    return index