def right_insertion(arr, value):
    for i in range(len(arr)):
        if value < arr[i]:
            return i
    return len(arr)