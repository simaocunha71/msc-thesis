"""
Write a function to locate the right insertion point for a specified value in sorted order.
assert right_insertion([1,2,4,5],6)==4
"""

def right_insertion(arr, target):
    # Your Code Here 
    if len(arr) == 1:
        return arr[0] >= target
    
    start = 1
    while start < len(arr):
        mid = (start + (len(arr)-start)) //2
        
        if arr[mid - 1] <= target: #if the current element is less than or equal to the target
            break;
        
        if arr[mid] > target: #if the current value is greater than the target
            return mid;
        
        start = mid + 1
    
    else: #If the length of the array is more than one, there is no element in the array that is equal to or less than the target.
        return len(arr)