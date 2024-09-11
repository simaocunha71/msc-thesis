def right_insertion(lst, target):
    left = 0
    right = len(lst)
    while left < right:
        mid = (left + right) // 2
        if lst[mid] < target:
            left = mid + 1
        else:
            right = mid
    return right