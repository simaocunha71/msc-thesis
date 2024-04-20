"""
Write a function to rotate a given list by specified number of items to the right direction. 
assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
"""

def rotate_right(list, n):
    """Rotate a given list by specified number of items to the right direction.
    Args:
        list (List[any type])
        n (int)
    Returns:
        A rotated list
    Raises:
        TypeError if one or more item in the input list cannot be casted into int"""
    
    # check that all items are of same type and castable to integer
    for i, val in enumerate(list):
        if not (isinstance(val, int) and 0 <= val < n + 1):
            raise TypeError("All the elements should be integer values")
    
    # create an empty list to return
    rotated_list = []
    
    # add all items in the input list to the end of rotated_list
    # except one or more items at index i-n
    for i, val in enumerate(list): 
        if not (i - n >= 0 and i <= len(list)): 
            rotated_list.append(val)
        
    return rotated_list