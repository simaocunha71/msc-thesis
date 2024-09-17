def right_insertion(sorted_list, value):
    left, right = 0, len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == value:
            return mid
        elif sorted_list[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return left