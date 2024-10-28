def check_min_heap(arr):
    n = len(arr) 
  
    # If last element is greater than its parent,
    # it means the array is not a min heap.
    for i in range(1, n): 
        if arr[i] < arr[(i - 1)//2] : 
            return False
    return True