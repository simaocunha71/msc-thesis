def right_insertion(arr, val):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < val:
            left = mid + 1
        else:
            right = mid
    return left if arr[left] < val else right