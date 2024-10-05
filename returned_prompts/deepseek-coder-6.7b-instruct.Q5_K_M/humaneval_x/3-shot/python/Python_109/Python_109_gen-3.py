    for i in range(len(arr)):
        if arr == sorted(arr[i:] + arr[:i]):
            return True
    return False


