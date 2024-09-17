def check_min_heap(arr):
    for i in range(len(arr)):
        if i == 0:
            continue
        if arr[i] < arr[i // 2]:
            return False
    return True