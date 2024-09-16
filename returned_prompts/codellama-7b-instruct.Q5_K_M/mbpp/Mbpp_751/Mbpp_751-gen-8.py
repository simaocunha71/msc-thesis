"""
def check_min_heap(arr):
    if len(arr) == 0:
        return True

    if len(arr) == 1:
        return True

    if len(arr) == 2:
        return True

    left_child_idx = 2 * idx + 1
    right_child_idx = 2 * idx + 2

    if left_child_idx > len(arr) or right_child_idx > len(arr):
        return True

    if arr[idx] > arr[left_child_idx] or arr[idx] > arr[right_child_idx]:
        return False

    return check_min_heap(arr[left_child_idx:]) and check_min_heap(arr[right_child_idx:])
"""