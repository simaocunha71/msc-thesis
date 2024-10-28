def check_min_heap(arr):
    # if array is empty
    if len(arr) == 0:
        return True

    # traverse for all nodes in heap
    for i in range(len(arr)):
        # left child
        left = (i + 1) * 2 - 1
        # right child
        right = (i + 1) * 2
        # left child is present in heap and its value is greater than parent node
        if left < len(arr) and arr[left] < arr[i]:
            return False
        # right child is present in heap and its value is greater than parent node
        if right < len(arr) and arr[right] < arr[i]:
            return False

    return True