    if not arr:
        return True

    original = arr[:]
    arr.sort()

    for _ in range(len(arr)):
        arr = arr[-1:] + arr[:-1]
        if arr == original:
            return True

    return False