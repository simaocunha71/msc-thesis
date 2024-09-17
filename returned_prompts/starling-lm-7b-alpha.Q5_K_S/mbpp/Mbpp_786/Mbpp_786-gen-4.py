
def right_insertion(sorted_list, insert_num):
    left = 0
    right = len(sorted_list)
    while left < right:
        mid = (left + right) // 2
        if sorted_list[mid] < insert_num:
            left = mid + 1
        else:
            right = mid
    return left


