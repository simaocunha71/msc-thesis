    if len(arr) == 0:
        return True

    sorted_arr = sorted(arr)
    for i in range(len(arr)):
        if arr[i:] + arr[:i] == sorted_arr:
            return True

    return False

