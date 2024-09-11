def left_insertion(sorted_list, value):
    left = 0
    right = len(sorted_list)
    while left < right:
        mid = (left + right) // 2
        if sorted_list[mid] < value:
            left = mid + 1
        else:
            right = mid
    return left