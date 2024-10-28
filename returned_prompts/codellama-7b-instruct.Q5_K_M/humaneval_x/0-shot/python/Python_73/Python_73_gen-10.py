
def smallest_change(arr):
    n = len(arr)
    # If array is already palindromic, return 0
    if arr == arr[::-1]:
        return 0

    # If array has only one element, return 1
    if n == 1:
        return 1

    # If array has two elements, return 1
    if n == 2:
        return 1

    # Initialize two arrays
    left = arr[:n//2]
    right = arr[n//2:]

    # Initialize two variables
    left_count = 0
    right_count = 0

    # Loop through the left array
    for i in range(n//2):
        if left[i] != left[n//2-1-i]:
            left_count += 1

    # Loop through the right array
    for i in range(n//2):
        if right[i] != right[n//2-1-i]:
            right_count += 1

    # Return the minimum of the two counts
    return min(left_count, right_count)
