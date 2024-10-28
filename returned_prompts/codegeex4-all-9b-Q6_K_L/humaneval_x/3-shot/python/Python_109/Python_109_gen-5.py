    if len(arr) == 0:
        return True
    if arr == sorted(arr):
        return True
    for i in range(1, len(arr)):
        if arr == sorted(arr[i:]+arr[:i]):
            return True
    return False

