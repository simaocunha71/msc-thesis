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

# Test the function
assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
assert check_min_heap([10, 15, 13, 20, 12, 50, 100, 200, 250]) == True
assert check_min_heap([100, 200, 150, 50, 60]) == False
<jupyter_output>
<empty_output>
<jupyter_text>
Heapify
<jupyter_code>
