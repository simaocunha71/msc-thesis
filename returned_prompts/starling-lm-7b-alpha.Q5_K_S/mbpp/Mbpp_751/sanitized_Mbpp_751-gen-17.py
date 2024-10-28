def check_min_heap(arr):
    # Check if the length of the array is less than 2 (min heap should have at least 2 elements)
    if len(arr) < 2:
        return False

    # Check if the root node is the smallest element
    if arr[0] > arr[1]:
        return False

    # Traverse through the array starting from the second element