def find_min_diff(arr,n):
    # Sort the array
    arr.sort()

    # Initialize the minimum difference
    min_diff = arr[1] - arr[0]

    # Loop through the array
    for i in range(1,n-1):
        diff = arr[i+1] - arr[i]

        # Check if the difference is smaller than the current minimum difference
        if diff < min_diff:
            min_diff = diff

    return min_diff