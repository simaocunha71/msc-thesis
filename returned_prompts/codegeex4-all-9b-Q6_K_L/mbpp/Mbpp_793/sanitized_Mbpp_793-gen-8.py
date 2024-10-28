def last(array, element):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == element:
            if mid == len(array) - 1 or array[mid + 1] != element:
                return mid
            else:
                low = mid + 1
        elif array[mid] < element:
            low = mid + 1
        else:
            high = mid - 1
    return -1