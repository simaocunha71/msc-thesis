def is_Monotonic(arr):
    # Check whether the array is monotonically increasing
    if all(arr[i] < arr[i+1] for i in range(len(arr)-1)):
        return True

    # Check whether the array is monotonically decreasing
    if all(arr[i] > arr[i+1] for i in range(len(arr)-1)):
        return True

    # If the array is not monotonically increasing or decreasing, then it is not monotonic
    return False
