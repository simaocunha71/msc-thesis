"""
def last(arr, elem):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == elem:
            right = mid - 1
        else:
            left = mid + 1
    return left - 1
"""
