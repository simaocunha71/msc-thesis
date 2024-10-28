def check_min_heap(arr):
    n = len(arr)
    for i in range(n//2, -1, -1):
        if i * 2 + 1 >= n or arr[i] < arr[i * 2 + 1]:
            return False
        if i * 2 + 2 >= n or arr[i] < arr[i * 2 + 2]:
            return False
    return True