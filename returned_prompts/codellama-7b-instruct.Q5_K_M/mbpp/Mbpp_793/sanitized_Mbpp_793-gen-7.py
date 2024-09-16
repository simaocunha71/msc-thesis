def last(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high and arr[high] != x:
        high -= 1
    return high