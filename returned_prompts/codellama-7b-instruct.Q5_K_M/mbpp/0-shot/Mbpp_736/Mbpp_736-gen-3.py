"""
def left_insertion(sorted_list, value):
    left = 0
    right = len(sorted_list)
    while left < right:
        middle = (left + right) // 2
        if sorted_list[middle] < value:
            left = middle + 1
        else:
            right = middle
    return left
"""
