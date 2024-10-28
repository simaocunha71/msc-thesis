def check_min_heap(arr):
    if not arr:
        return True
    for i in range(len(arr)):
        if 2*i + 1 < len(arr) and arr[i] > arr[2*i + 1]:
            return False
        if 2*i + 2 < len(arr) and arr[i] > arr[2*i + 2]:
            return False
    return True