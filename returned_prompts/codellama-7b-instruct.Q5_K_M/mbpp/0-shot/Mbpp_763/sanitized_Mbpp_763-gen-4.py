def find_min_diff(arr):
    # Sort the array
    arr.sort()
    # Initialize the minimum difference to infinity
    min_diff = float("inf")
    # Loop through the array
    for i in range(len(arr)-1):
        # Find the difference between the current element and the next element
        diff = arr[i+1]-arr[i]
        # Check if the difference is less than the minimum difference
        if diff < min_diff:
            # Update the minimum difference
            min_diff = diff
    return min_diff