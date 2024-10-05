    # Check if array is already palindromic
    if arr == arr[::-1]:
        return 0

    # Initialize count of changes
    changes = 0

    # Initialize two pointers for the start and end of the array
    left, right = 0, len(arr) - 1

    # Loop until the two pointers meet
    while left < right:
        # If the left and right elements are not equal, increment changes
        if arr[left] != arr[right]:
            changes += 1
        # Move the pointers towards the center
        left += 1
        right -= 1

    return changes
# Test the function
print(smallest_change([1,2,3,5,4,7,9,6]))  # Output: 4
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))  # Output: 1
print(smallest_change([1, 2, 3, 2, 1]))  # Output: 0
# Note: This solution has a time complexity of O(n) and a space complexity of O(1), where n is the length of the input array.