def is_Monotonic(arr):
    if arr == sorted(arr):
        return True
    if arr == sorted(arr, reverse=True):
        return True
    return False