def left_insertion(arr, val):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    left = -1
    right = len(arr)
    while right - left > 1:
        mid = (left + right) // 2
        if arr[mid] < val:
            left = mid
        else:
            right = mid
    return left