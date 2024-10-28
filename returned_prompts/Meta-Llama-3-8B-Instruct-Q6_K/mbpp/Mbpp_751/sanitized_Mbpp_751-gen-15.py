def check_min_heap(arr):
    if len(arr) < 1:
        return True
    for i in range(len(arr)):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(arr) and arr[i] > arr[left]:
            return False
        if right < len(arr) and arr[i] > arr[right]:
            return False
    return True