    for i in range(len(arr)):
        if arr[i:] + arr[:i] == sorted(arr):
            return True
    return False


