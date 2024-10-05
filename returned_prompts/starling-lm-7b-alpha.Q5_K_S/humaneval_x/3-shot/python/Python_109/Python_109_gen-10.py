    def is_sorted(arr):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                return False
        return True

    if len(arr) == 0:
        return True

    for i in range(len(arr)):
        arr_copy = arr[:i] + [arr[i]] + arr[i+1:]
        if is_sorted(arr_copy):
            return True
    return False


