

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    
    new_str = ''
    for ch in string:
        if 'a' <= ch < 'z': # lowercase to upper, and the rest is untouched
            new_str += chr((ord(ch) - 32) + 32)
        else:                 # uppercase to lower and everything else is touched
            new_str += chr((ord(ch) + 32))
    
    return new_str.lstrip()


def flip_case(string: str, case_type: str='a') -> str:
    """ For a given string and the case_type argument, flip lowercase characters to uppercase or vice versa. 
    >>> flip_case('Hello', 'a')
    'hELLo'
    >>> flip_case('Hello', 'u') # flip all letters to uppercase
    'HELLO'
    """