def right_insertion(lst, value):
    left, right = 0, len(lst)
    while left < right:
        mid = (left + right) // 2
        if lst[mid] < value:
            left = mid + 1
        else:
            right = mid
    return left