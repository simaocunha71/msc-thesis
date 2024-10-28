
def smallest_change(arr):
    # Write your solution here
    # Edge case: empty array
    if not arr:
        return 0
    # Edge case: single element
    if len(arr) == 1:
        return 0
    # Edge case: array is already a palindrome
    if arr == arr[::-1]:
        return 0
    # Sort the array
    arr.sort()
    # Initialize variables
    min_changes = 0
    max_value = arr[-1]
    # Loop through the array
    for i in range(len(arr) - 1):
        # If the current value is not equal to the max value, and the next value is not equal to the current value
        # then we need to make a change
        if arr[i] != max_value and arr[i + 1] != arr[i]:
            min_changes += 1
    # Return the minimum number of changes
    return min_changes





























