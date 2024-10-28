def is_Monotonic(arr):
    is_increasing = arr[0] <= arr[1]
    is_decreasing = arr[0] >= arr[1]
    for i in range(2, len(arr)):
        if (arr[i] > arr[i-1]) != is_increasing:
            is_increasing = False
        if (arr[i] < arr[i-1]) != is_decreasing:
            is_decreasing = False
    return is_increasing or is_decreasing