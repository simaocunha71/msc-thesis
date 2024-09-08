def check_min_heap(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[(i-1)//2]:
            return False
    return True