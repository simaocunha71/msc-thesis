def find_Rotations(s):
    # Convert string to list
    lst = list(s)
    
    # Sort the list
    lst.sort()
    
    # Convert list to string
    sorted_s = ''.join(lst)
    
    # Find the index where the string starts to repeat itself
    index = s.find(sorted_s)
    
    # If the index is not 0, then the minimum number of rotations required will be index + 1
    if index != 0:
        return index + 1
    
    # If the index is 0, then the string is already in sorted order and the minimum number of rotations required will be 1
    return 1