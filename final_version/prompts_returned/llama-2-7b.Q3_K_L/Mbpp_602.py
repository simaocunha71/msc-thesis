"""
Write a python function to find the first repeated character in a given string.
assert first_repeated_char("abcabc") == "a"
"""
# Time Complexity: O(n)
# Space Complexity: O(1) where n is the length of the input string s
def first_repeat_character(s):
    """
    :param s: string to be checked for repeated characters
    :return: index of repeated character or -1 if none exists.
    """
    
    # Check if there are any repeated characters in a given string s. 
    if len(set(s)) == 0: 
        return -1
    
    # Store the index of repeated character. 
    first_char = None 
    
    for char in s:
        
        # If current character is different from all previous characters, store it's index and break out of loop.
        if char != first_char:
            
            # Since the first character in string was not repeated, return -1. 
            if char == None:
                return -1
                    
            # Store current index of repeated character as first_char variable. 
            first_char = s.index(first_char)
            
    else:
        
        # If current character is same as the first, return it's index
        first_char = s.index(first_char) if char != None else -1
    
    return first_char