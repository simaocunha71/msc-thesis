def check_min_heap(arr):
    if len(arr) == 0:
        return False
    if len(arr) == 1:
        return True
    for i in range(len(arr)):
        if i == 0:
            continue
        if arr[i] < arr[i // 2 - 1]:
            return False
    return True