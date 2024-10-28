def left_insertion(arr, x):
    'Locate the left insertion point for a specified value in sorted order.'
    for i in range(len(arr)):
        if arr[i] > x:
            return i
    return len(arr)