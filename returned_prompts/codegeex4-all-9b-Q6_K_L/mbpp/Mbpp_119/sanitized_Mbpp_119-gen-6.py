def search(arr):
    # Initialize pointers
    left = 0
    right = len(arr) - 1

    # Loop until pointers meet
    while left < right:
        mid = left + (right - left) // 2

        # Check if mid is odd or even
        if mid % 2 == 1:
            mid -= 1

        # If the pair at mid is equal, the single element is in the right half
        if arr[mid] == arr[mid + 1]:
            left = mid + 2
        else:
            right = mid

    # The left pointer will be at the single element
    return arr[left]