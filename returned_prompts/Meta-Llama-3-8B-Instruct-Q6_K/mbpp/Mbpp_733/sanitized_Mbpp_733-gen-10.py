def find_first_occurrence(sorted_array, target):
    start, end = 0, len(sorted_array) - 1
    while start <= end:
        mid = (start + end) // 2
        if sorted_array[mid] == target:
            if mid == 0 or sorted_array[mid - 1] != target:
                return mid
            end = mid - 1
        elif sorted_array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1  # not found