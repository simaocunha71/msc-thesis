"""
def left_insertion(arr, value):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= value:
            right = mid - 1
        else:
            left = mid + 1
    return left
"""
