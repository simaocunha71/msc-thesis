def left_insertion(arr, val):
    """
    Time: O(log n)
    Space: O(1)
    """
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
    return left
arr = [1, 2, 4, 5]
val = 6