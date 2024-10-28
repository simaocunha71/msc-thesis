
def match_parens(lst):
    """
    Returns 'Yes' if the list of parentheses is balanced, 'No' otherwise
    """
    stack = []
    for char in lst:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                return 'No'
            stack.pop()
    return 'Yes' if not stack else 'No'
