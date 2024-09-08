def check_min_heap(arr):
    n = len(arr)
    for i in range(int(n/2)):
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        if left_child < n and arr[i] > arr[left_child]:
            return False
        if right_child < n and arr[i] > arr[right_child]:
            return False
    return True