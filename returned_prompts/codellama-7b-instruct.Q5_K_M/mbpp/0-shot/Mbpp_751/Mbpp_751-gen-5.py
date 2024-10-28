def check_min_heap(arr):
    # If the given array is empty, then it is a heap.
    if not arr:
        return True

    # If the given array has only one element, then it is a heap.
    if len(arr) == 1:
        return True

    # If the given array has more than one element, then check if the root is less than its children.
    if arr[0] > arr[1]:
        return False

    # If the given array has more than two elements, then check if the root is less than its children.
    if len(arr) > 2 and arr[0] > arr[2]:
        return False

    # If the given array is not a heap, then return False.
    return check_min_heap(arr[1:])


