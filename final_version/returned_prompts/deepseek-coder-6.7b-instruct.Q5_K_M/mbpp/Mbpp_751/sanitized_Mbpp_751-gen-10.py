def check_min_heap(arr):
    n = len(arr) 
  
    # If last parent node is greater than its children, then it is not a min heap
    for i in range(int(n/2)): 
        if arr[i] > arr[2 * i + 1]: 
            return False
        if 2 * i + 2 < n: 
            if arr[i] > arr[2 * i + 2]: 
                return False
    return True