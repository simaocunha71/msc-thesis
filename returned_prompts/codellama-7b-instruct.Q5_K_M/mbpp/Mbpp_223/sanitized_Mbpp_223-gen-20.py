def is_majority(arr, n, ele):
    # Check if the input array is valid
    if arr is None or n < 0:
        return False

    # Check if the element is present more than n/2 times
    freq = 0
    for i in range(n):
        if arr[i] == ele:
            freq += 1
        if freq > n/2:
            return True
    return False