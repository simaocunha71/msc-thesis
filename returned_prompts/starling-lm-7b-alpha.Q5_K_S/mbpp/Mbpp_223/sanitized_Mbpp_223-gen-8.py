def is_majority(arr, n, element):
    # Get the middle index of the array
    mid = n // 2
    # Check if the element is the middle element of the array
    if element == arr[mid]:
        # Get the left and right neighbor of the middle element
        left_neighbor = arr[mid - 1] if mid > 0 else -1
        right_neighbor = arr[mid + 1] if mid < n - 1 else -1
        # If both neighbors are equal to the middle element, return True
        if left_neighbor == element and right_neighbor == element:
            return True
    # If the element is not the middle element, return False
    return False