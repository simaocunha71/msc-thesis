def check_min_heap(arr):
    for i in range(len(arr)):
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        if left_child < len(arr) and arr[left_child] < arr[i]:
            return False
        if right_child < len(arr) and arr[right_child] < arr[i]:
            return False
    return True

