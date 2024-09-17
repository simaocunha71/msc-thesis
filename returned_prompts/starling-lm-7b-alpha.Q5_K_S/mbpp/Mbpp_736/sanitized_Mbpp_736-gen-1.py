def left_insertion(sorted_list, value):
    left = 0
    right = len(sorted_list) - 1
    while left < right:
        if value < sorted_list[(left + right) // 2]:
            right = (left + right) // 2 - 1
        else:
            left = (left + right) // 2 + 1
    return left