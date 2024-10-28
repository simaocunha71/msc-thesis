def check_min_heap(arr):
    if len(arr) == 0 or len(arr) == 1:
        return True
    left = 2 * idx + 1
    right = 2 * idx + 2
    if left >= len(arr) and right >= len(arr):
        return True
    if left < len(arr) and arr[left] < arr[idx]:
        return False
    if right < len(arr) and arr[right] < arr[idx]:
        return False
    return check_min_heap(arr[left:]) and check_min_heap(arr[right:])