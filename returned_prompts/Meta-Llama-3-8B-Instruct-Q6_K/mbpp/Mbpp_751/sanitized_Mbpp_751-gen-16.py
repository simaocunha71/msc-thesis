def check_min_heap(arr):
    for i in range(len(arr)):
        if i*2+1 < len(arr) and arr[i*2+1] < arr[i]:
            return False
    return True