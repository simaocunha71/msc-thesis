def left_insertion(arr, val):
    if val < arr[0]:
        return 0
    for i in range(1, len(arr)):
        if val <= arr[i]:
            return i
    return len(arr)