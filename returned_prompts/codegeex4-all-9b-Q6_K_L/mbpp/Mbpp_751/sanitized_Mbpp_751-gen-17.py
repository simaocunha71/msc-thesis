def check_min_heap(arr):
    if len(arr) <= 1:
        return True
    for i in range(len(arr)):
        if i*2+1 < len(arr) and arr[i] > arr[i*2+1]:
            return False
        if i*2+2 < len(arr) and arr[i] > arr[i*2+2]:
            return False
    return True