def last(sorted_array, target):
    low = 0
    high = len(sorted_array) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_array[mid] < target:
            low = mid + 1
        elif sorted_array[mid] > target:
            high = mid - 1
        else:
            if mid == len(sorted_array) - 1 or sorted_array[mid + 1] != target:
                return mid
            high = mid - 1
    return -1