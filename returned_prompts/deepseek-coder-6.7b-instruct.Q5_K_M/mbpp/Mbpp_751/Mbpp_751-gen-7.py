def check_min_heap(arr):
    n = len(arr) 
  
    # Iterate through every item of array
    for i in range(int(n/2) - 1): 
        # If left child is greater than parent 
        if arr[i] > arr[2*i + 1]: 
            return False
  
        # If right child exists and is greater than parent 
        if 2*i + 2 < n: 
            if arr[i] > arr[2*i + 2]: 
                return False
              
    return True

print(check_min_heap([1, 2, 3, 4, 5, 6])) # Should return True

"""
