def check_min_heap(arr):
    n = len(arr)
    for i in range(n):
        left = 2*i + 1
        right = 2*i + 2
        if left < n and arr[i] > arr[left]:
            return False
        if right < n and arr[i] > arr[right]:
            return False
    return True