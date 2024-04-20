"""
Write a function to check whether a specified list is sorted or not.
assert issort_list([1,2,4,6,8,10,12,14,16,17])==True
"""

def issort(lst):
    if type(lst) != type([]): # Checking the type of list
        raise TypeError("List should be a List type")
        
    if len(lst) < 2:
        return True
    
    for i in range(len(lst)-1,-1,-1):
        if lst[i]>lst[i-1]: # Checking is the list sorted or not
            return False
            
    return True
        
        
"""Write a function to check whether a specified list is sorted or not.
assert issort_list([5, 4, 3, 2, 1])==True
"""
