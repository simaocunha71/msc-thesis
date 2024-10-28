def check_min_heap(arr):
    if len(arr) == 1:
        return True
    left = 2 * i + 1
    right = 2 * i + 2
    if left >= len(arr) or right >= len(arr):
        return True
    if arr[i] > arr[left] or arr[i] > arr[right]:
        return False
    return check_min_heap(arr[left:]) and check_min_heap(arr[right:])