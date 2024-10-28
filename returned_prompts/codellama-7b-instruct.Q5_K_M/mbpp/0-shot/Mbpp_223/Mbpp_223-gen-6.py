"""
def is_majority(arr, n, x):
    # Edge case: If the length of the array is 1, the only element is the majority element.
    if n == 1:
        return True
    
    # Edge case: If the length of the array is 0, there is no majority element.
    if n == 0:
        return False
    
    # The majority element must occur more than n/2 times.
    # The first element in the array is the majority element if it occurs more than n/2 times.
    if arr[0] == x and arr.count(arr[0]) > n/2:
        return True
    
    # If the first element in the array is not the majority element, the last element in the array is the majority element if it occurs more than n/2 times.
    if arr[-1] == x and arr.count(arr[-1]) > n/2:
        return True
    
    # The majority element must occur more than n/2 times.
    # If the first element in the array does not occur more than n/2 times, the last element in the array must occur more than n/2 times.
    if arr.count(arr[0]) <= n/2 and arr.count(arr[-1]) > n/2:
        return True
    
    # If the first element in the array does not occur more than n/2 times, the last element in the array does not occur more than n/2 times, the majority element must occur more than n/2 times in the middle of the array.
    else:
        # The middle index of the array.
        mid = n//2
        
        # If the majority element is in the middle of the array, return True.
        if arr[mid] == x and arr.count(arr[mid]) > n/2:
            return True
        
        # If the majority element is not in the middle of the array, return False.
        else:
            return False
"""
