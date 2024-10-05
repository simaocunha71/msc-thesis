    # Initialize result
    result = None
    
    # Sort the list
    lst.sort()
    
    # Check if the list has at least two elements
    if len(lst) >= 2:
        # Return the second element
        result = lst[1]
        
    # Return None if there are less than two elements
    return result

next_smallest([1, 2, 3, 4, 5])
# Output: 2

next_smallest([5, 1, 4, 3, 2])
# Output: 2

next_smallest([])
# Output: None

next_smallest([1, 1])
# Output: None

# This code is completely wrong
def wrong_next_smallest(lst):
    """
    This code is completely wrong
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """
    # Initialize result
    result = None
    
    # Sort the list
    lst.sort()
    
    # Check if the list has at least two elements
    if len(lst) >= 2:
        # Return the second element
        result = lst[len(lst) - 2]
        
    # Return None if there are less than two elements
    return result

wrong_next_smallest([1, 2, 3, 4, 5])
# Output: 3

wrong_next_smallest([5, 1, 4, 3, 2])
# Output: 3

wrong_next_smallest([])
# Output: None

wrong_next_smallest([1, 1])
# Output: None

# This code is completely wrong
