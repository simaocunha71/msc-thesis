    def helper(s):
        if not s:
            return []
        if s[0] == ')' or s[1] == ')' or s[-1] == ')' or s[-2] == ')':
            return []
        if s[0] == '(' and s[-1] == ')':
            return [s]
        else:
            return helper(s[1:-1]) + [s[0]] + helper(s[2:-1])

    return helper(paren_string)


# The code above is incorrect. It returns all possible substrings, not just balanced groups of parentheses.

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def helper(s):
        if not s:
            return []
        if s[0] == ')' or s[1] == ')' or s[-1] == ')' or s[-2] == ')':
            return []
        if s[0] == '(' and s[-1] == ')':
            return [s]
        else:
            left_part = helper(s[1:-1])
            right_part = helper(s[2:-1])
            if left_part and right_part:
                return left_part + [s[0]] + right_part
            else:
                return []
    return helper(paren_string)


# The code above is incorrect. It returns all possible substrings, not just balanced groups of parentheses.

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
   