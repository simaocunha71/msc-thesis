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

print(check_min_heap([1, 2, 3, 4, 5, 6]))
"""
In the code above, the function check_min_heap checks if the array represents a min heap or not.
If the array represents a min heap, it will return True, otherwise it will return False.
"""
<jupyter_output>
True
<jupyter_text>
Question 3
<jupyter_code>
