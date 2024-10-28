
def last(arr, elem):
    if not arr:
        return -1
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == elem:
            left = mid + 1
        else:
            right = mid - 1
    return right


