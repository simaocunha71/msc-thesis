def is_Monotonic(arr):
    n = len(arr)
    if n == 1:
        return True
    for i in range(1, n):
        if arr[i] != arr[i-1]:
            if arr[i] > arr[i-1]:
                if not all(arr[i] >= x for x in arr[i+1:]):
                    return False
            elif arr[i] < arr[i-1]:
                if not all(arr[i] <= x for x in arr[i+1:]):
                    return False
    return True


