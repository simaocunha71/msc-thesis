def right_insertion(lst, v):
    left = 0
    right = len(lst)
    while left < right:
        mid = (left + right) // 2
        if lst[mid] > v:
            right = mid
        else:
            left = mid + 1
    return left