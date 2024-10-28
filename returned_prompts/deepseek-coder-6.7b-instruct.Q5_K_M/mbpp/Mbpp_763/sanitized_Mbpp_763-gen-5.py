def find_min_diff(arr, n):

    # Initialize difference as infinite
    diff = float('inf')

    # Sort array elements
    arr = sorted(arr)

    # Find the min diff by comparing adjacent pairs in sorted array
    for i in range(n-1):
        if arr[i+1] - arr[i] < diff:
            diff = arr[i+1] - arr[i]

    # Return min diff
    return diff