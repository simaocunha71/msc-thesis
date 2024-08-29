def check_min_heap(lst):
    n = len(lst)
  
    # Iterate through every item of the array
    for i in range(int(n/2)-1):
        # If left child is greater than parent 
        if lst[i] > lst[2 * i + 1]:
            return False
  
        # If right child exists and is greater than parent 
        if 2 * i + 2 < n:
            if lst[i] > lst[2 * i + 2]:
                return False
              
    return True

assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
"""
This program works by checking each element in the list, if the element is not less than its children, then the list does not represent a min heap.
"""

"""
