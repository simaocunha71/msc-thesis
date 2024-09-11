def check_min_heap(arr):
    # Check if array is empty
    if len(arr) == 0:
        return False

    # Check if the array represents a min heap
    for i in range(len(arr) // 2 - 1, -1, -1):
        if arr[i] > arr[2 * i + 1] or (2 * i + 2 < len(arr) and arr[i] > arr[2 * i + 2]):
            return False
    return True