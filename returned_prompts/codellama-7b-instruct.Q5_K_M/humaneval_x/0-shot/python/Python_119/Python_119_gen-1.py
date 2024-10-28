
def match_parens(lst):
    # Check if the strings are balanced
    if not balanced(lst):
        return 'No'

    # Check if the strings are concatenatable
    if not concatenatable(lst):
        return 'No'

    return 'Yes'

def balanced(lst):
    # Count the number of open parentheses
    count = 0
    for c in lst:
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0

def concatenatable(lst):
    # Check if the strings are concatenatable
    count = 0
    for c in lst:
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
        if count < 0:
            return False
    return True
