def check_min_heap(arr):
    n = len(arr)
    
    # Iterate through middle elements
    for i in range(int(n/2)):
        # If left child is greater than parent
        if arr[i] > arr[2 * i + 1]:
            return False
 
        # If right child exists and is greater than parent
        if 2 * i + 2 < n:
            if arr[i] > arr[2 * i + 2]:
                return False
             
    return True