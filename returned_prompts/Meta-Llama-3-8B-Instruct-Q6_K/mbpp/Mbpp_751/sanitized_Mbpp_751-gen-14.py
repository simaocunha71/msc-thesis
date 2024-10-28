def check_min_heap(arr):
    n = len(arr)
    if arr[0] > min(arr):
        return False
    for i in range(1, n):
        if arr[i-1] > arr[i]:
            return False
    return True