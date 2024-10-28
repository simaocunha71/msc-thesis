def last(arr, target):
    for i in reversed(range(len(arr))):
        if arr[i] == target:
            return i
    return -1