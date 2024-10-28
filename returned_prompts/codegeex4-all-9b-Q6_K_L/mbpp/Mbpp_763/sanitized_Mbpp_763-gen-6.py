def find_min_diff(arr, n):
    arr.sort()  # Sort the array in ascending order
    min_diff = arr[1] - arr[0]  # Initialize min_diff with the difference between the first two elements
    for i in range(2, n):
        diff = arr[i] - arr[i-1]
        min_diff = min(min_diff, diff)  # Update min_diff with the minimum difference
    return min_diff