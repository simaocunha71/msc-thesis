
def check_min_heap(arr):
    n = len(arr)
    if n == 0 or n == 1:
        return True
    i = 1
    while i < n // 2:
        if arr[i] < arr[i // 2]:
            return False
        i += 1
    return True


