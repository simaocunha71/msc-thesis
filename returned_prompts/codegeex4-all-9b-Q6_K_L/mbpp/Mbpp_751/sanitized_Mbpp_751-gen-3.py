def check_min_heap(arr):
    n = len(arr)
    for i in range(n):
        if 2*i + 1 < n and arr[i] > arr[2*i + 1]:
            return False
        if 2*i + 2 < n and arr[i] > arr[2*i + 2]:
            return False
    return True