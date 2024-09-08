def left_insertion(arr, val):
    # Initialize the left and right pointers
    left, right = 0, len(arr)
    
    # Perform binary search to find the left insertion point
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < val:
            left = mid + 1
        else:
            right = mid
    
    # Return the left insertion point
    return left