

def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
    
    return s0 == s1 and len(s0) == len(s1)
def longest_common_prefix(s1: str, s2: str):
    """Get the common prefix of two words.
    >>> longest_common_prefix('a', 'bb')
    'b'
    >>> longest_common_prefix('d', 'fedcba')
    ''
    >>> longest_common_prefix('fe', 'fedcba')
    'ef'
    """
    
    for c in s1:
        if c not in s2:
            return "".join([c])
        
    return ""