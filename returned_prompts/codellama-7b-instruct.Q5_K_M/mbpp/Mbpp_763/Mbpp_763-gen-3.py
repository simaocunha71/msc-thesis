```
def find_min_diff(arr, n):
    # Find the minimum difference between any two elements in arr
    # Sort the array in ascending order
    arr.sort()
    # Initialize minimum difference as infinite
    min_diff = float("inf")
 
    # Loop through the array
    for i in range(n - 1):
        # Calculate the difference between current element and the next element
        diff = arr[i + 1] - arr[i]
        # If the difference is less than the current minimum difference, update the minimum difference
        if diff < min_diff:
            min_diff = diff
 
    # Return the minimum difference
    return min_diff

```
