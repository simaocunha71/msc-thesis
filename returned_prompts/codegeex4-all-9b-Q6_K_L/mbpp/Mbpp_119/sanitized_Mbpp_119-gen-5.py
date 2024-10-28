def search(arr):
    # Initialize two pointers
    left = 0
    right = len(arr) - 1

    # Loop until the pointers meet
    while left < right:
        mid = (left + right) // 2

        # Check if the middle element is the only one
        if arr[mid] != arr[mid - 1] and arr[mid] != arr[mid + 1]:
            return arr[mid]

        # If the middle element is the same as the previous one, search in the right half
        elif arr[mid] == arr[mid - 1]:
            left = mid + 1

        # If the middle element is the same as the next one, search in the left half
        else:
            right = mid - 1

    # If the loop finishes without finding the element, return None
    return None