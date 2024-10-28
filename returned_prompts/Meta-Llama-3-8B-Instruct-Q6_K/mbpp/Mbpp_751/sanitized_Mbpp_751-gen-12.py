def check_min_heap(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[i//2] > arr[i]:
            return False
    return True