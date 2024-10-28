
def left_insertion(arr, num):
    for i in range(len(arr)):
        if arr[i] > num:
            return i
    return len(arr)


