def left_insertion(arr, value):
    """
    Time: O(log n)
    Space: O(1)
    """
    left = 0
    right = len(arr) - 1
    mid = 0
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return mid