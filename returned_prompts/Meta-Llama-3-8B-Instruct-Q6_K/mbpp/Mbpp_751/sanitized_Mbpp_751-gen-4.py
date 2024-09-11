def check_min_heap(arr):
    if len(arr) == 0:
        return True
    for i in range(len(arr)):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(arr) and arr[left] < arr[i]:
            return False
        if right < len(arr) and arr[right] < arr[i]:
            return False
    return True