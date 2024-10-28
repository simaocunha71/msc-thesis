def right_insertion(l, k):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] == k:
            return mid
        elif l[mid] > k:
            high = mid - 1
        else:
            low = mid + 1
    return low