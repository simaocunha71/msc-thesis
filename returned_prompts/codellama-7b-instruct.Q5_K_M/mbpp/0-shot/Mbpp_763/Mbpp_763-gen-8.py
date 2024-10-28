def find_min_diff(arr, n):
    # Sort the array elements in ascending order
    arr.sort()
    # Initialize the minimum difference
    min_diff = sys.maxsize
    # Loop through all the elements
    for i in range(n - 1):
        # Find the minimum difference between any two elements
        diff = arr[i + 1] - arr[i]
        # If the difference is less than the current minimum difference, update it
        if diff < min_diff:
            min_diff = diff
    # Return the minimum difference
    return min_diff
