    if not arr:
        return True
    arr.sort()
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            continue
        if arr[i] < arr[i + 1]:
            continue
        else:
            return False
    return True


