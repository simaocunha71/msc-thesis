
def left_insertion(sorted_list: list, value: int) -> int:
    left = 0
    right = len(sorted_list) - 1
    while left < right:
        mid = (left + right) // 2
        if value < sorted_list[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return left


