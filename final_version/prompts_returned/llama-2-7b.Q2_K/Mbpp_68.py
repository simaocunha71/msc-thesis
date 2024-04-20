"""
Write a python function to check whether the given array is monotonic or not.
assert is_Monotonic([6, 5, 4, 4]) == True
"""

def is_Monotonic(arr):
    if arr == []: 
        return False
    else:    
        for i in range(0,len(arr)-1):
            prev = arr[i]
            curr = arr[i+1]
            
            if (curr < prev) and (not is_Monotonic([curr])):
                # the new value should come after the previous one.
                return False
        return True
