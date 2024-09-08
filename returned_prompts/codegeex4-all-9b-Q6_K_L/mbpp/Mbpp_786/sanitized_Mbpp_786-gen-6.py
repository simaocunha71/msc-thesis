def right_insertion(sorted_list, value):
    low = 0
    high = len(sorted_list)
    while low < high:
        mid = (low + high) // 2
        if sorted_list[mid] < value:
            low = mid + 1
        else:
            high = mid
    return low