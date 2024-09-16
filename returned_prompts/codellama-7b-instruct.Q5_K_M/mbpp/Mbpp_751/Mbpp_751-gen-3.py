def check_min_heap(arr):
    if len(arr) == 0 or len(arr) == 1:
        return True
    if arr[0] > arr[1]:
        return False
    left = arr[1]
    right = arr[2]
    if left > right:
        return False
    for i in range(2, len(arr)):
        left = arr[i*2-1]
        right = arr[i*2]
        if left > right:
            return False
    return True

