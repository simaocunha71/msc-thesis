def is_Monotonic(arr):
    increasing = decreasing = True
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            decreasing = False
        if arr[i-1] < arr[i]:
            increasing = False
    return increasing or decreasing