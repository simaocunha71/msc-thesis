    arr = list(set(arr))
    arr.sort()

    low = 0
    high = len(arr) - 1

    while low < high:
        arr[low] = arr[high]
        low += 1
        high -= 1

    return len(arr) - len(set(arr))


