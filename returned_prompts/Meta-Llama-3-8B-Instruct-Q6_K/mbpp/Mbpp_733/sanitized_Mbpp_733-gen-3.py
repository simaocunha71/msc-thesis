def find_first_occurrence(sorted_array, target):
    left, right = 0, len(sorted_array) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_array[mid] == target:
            if mid == 0 or sorted_array[mid - 1] != target:
                return mid
            right = mid - 1
        elif sorted_array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1