def left_insertion(array, value):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return left