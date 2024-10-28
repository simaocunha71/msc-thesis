def find_min_diff(arr,n):
    # Sort the array
    arr.sort()
    # Initialize the minimum difference
    min_diff = arr[1] - arr[0]
    # Loop through the array
    for i in range(1,n):
        # Calculate the difference between two consecutive elements
        diff = arr[i] - arr[i-1]
        # Check if the difference is smaller than the minimum difference
        if diff < min_diff:
            # Update the minimum difference
            min_diff = diff
    return min_diff