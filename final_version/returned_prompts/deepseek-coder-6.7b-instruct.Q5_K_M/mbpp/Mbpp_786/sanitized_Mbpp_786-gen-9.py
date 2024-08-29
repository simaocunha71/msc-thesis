def right_insertion(arr, val):
    for i in range(len(arr)):
        if arr[i]>val:
            return i
    return len(arr)