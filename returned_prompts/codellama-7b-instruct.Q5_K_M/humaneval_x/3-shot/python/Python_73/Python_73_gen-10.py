    # Sort the list
    arr = sorted(arr)

    # Initialize the variables
    min_changes = 0
    left = 0
    right = len(arr) - 1

    # Loop through the list
    while left < right:
        # Check if the elements are equal
        if arr[left] == arr[right]:
            left += 1
            right -= 1
        else:
            # Check if the right element is the next closest element
            if abs(arr[left] - arr[right]) == 1:
                right -= 1
            # Otherwise increase the number of changes
            else:
                min_changes += 1
                left += 1

    return min_changes


