def is_Monotonic(arr: list) -> bool:
    isMonotonic = True
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            isMonotonic = False
            break
    return isMonotonic