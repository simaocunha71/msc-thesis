
def check_min_heap(arr):
    n = len(arr)
    if n == 0 or n == 1:
        return True
    i = 1
    while i < n:
        left = 2 * i
        right = 2 * i + 1
        if left < n and arr[i] > arr[left]:
            return False
        if right < n and arr[i] > arr[right]:
            return False
        i += 1
    return True


