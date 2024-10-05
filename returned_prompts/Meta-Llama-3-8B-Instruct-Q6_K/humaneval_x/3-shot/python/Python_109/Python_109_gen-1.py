    arr = arr.copy()
    arr.sort()
    if len(arr) == 0:
        return True
    for num in arr:
        if num != arr[0]:
            return False
        arr.pop(0)
        arr.append(arr.pop(0))
    return True


