def is_Monotonic(arr):
    is_non_decreasing = True
    is_non_increasing = True
    
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            is_non_decreasing = False
        if arr[i] < arr[i + 1]:
            is_non_increasing = False
    
    return is_non_decreasing or is_non_increasing