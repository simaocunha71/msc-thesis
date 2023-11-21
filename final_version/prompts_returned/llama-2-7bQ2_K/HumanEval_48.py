

def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    
    for c in text:
        if c == 'd' and not(text[len(text)-1]==c): break
        elif c == 'a':
            if text[-1] != 'a': break
            
    return True if is_palindrome('') else False 