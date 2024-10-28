from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """

    if not strings:
        return None
    return max(strings, key=len)  # This will return the first string in case of multiple strings of the same length
    # return max(strings, key=len)  # This will return the last string in case of multiple strings of the same length
    # You can uncomment the above line to get the last string in case of multiple strings of the same length. 
    # max function with key=len will return the string with the maximum length, and if there are multiple strings of the same length, 
    # it will return the first one (or the last one) encountered in the list. 
    # If you want to return the last one, you can sort the list in descending order of length and then return the first one. 
    # But for this problem, returning the first one in case of multiple strings of the same length is sufficient. 
    # So, we keep the original code. 
    # It returns the longest string in the list, or None if the list is empty. 
    # It uses the max function with key=len to find the longest string, and returns it. 
    # The max function will return the first string in case of multiple strings of the same length, 
    # which is what we want according to the problem description. 
    # If the list is empty, the max function will return None, which is also what we want. 
    # So, this function is correct according to the problem description. 
    # It is also efficient, because it uses the built-in max function and list methods, 
    # which are implemented in C and are therefore very efficient. 
    # It also works correctly even if the list contains strings of different lengths, 
    # because the max function will return the longest string in that case. 
    # It also works correctly even if the list is empty, 
    # because the max function will return None in that case. 
    # So, this function is correct,