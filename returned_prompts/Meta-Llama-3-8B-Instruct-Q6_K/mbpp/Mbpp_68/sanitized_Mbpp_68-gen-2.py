def is_Monotonic(arr):
    if arr == sorted(arr) or arr == sorted(arr, reverse=True):
        return True
    else:
        return False