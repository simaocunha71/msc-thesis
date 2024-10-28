def check_min_heap(arr):
    n = len(arr)

    # Iterate from the first index till the last index
    for i in range(n):
        # If left child exists
        if 2*i+1 < n:
            # If parent is greater than left child
            if arr[i] > arr[2*i+1]:
                return False
        # If right child exists
        if 2*i+2 < n:
            # If parent is greater than right child
            if arr[i] > arr[2*i+2]:
                return False
    # If none of the above conditions is true, array represents min heap
    return True