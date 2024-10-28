def is_Monotonic(arr):
    is_increasing = False
    is_decreasing = False
    
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            is_increasing = True
        elif arr[i] < arr[i-1]:
            is_decreasing = True
        else:
            continue
    
    return is_increasing or is_decreasing