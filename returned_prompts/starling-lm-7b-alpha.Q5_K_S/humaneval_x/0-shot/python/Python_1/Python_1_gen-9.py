    def helper(s):
        res = []
        count = 0
        for i in range(len(s)):
            if s[i] == '(':
                count += 1
            elif s[i] == ')':
                count -= 1
            if count == 0:
                res.append(s[i-1:i+1])
        return res

    res = []
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            count = 1
            for j in range(i + 1, len(paren_string)):
                if paren_string[j] == '(':
                    count += 1
                elif paren_string[j] == ')':
                    count -= 1
                if count == 0:
                    res.append(paren_string[i:j+1])
                    break
    return res

# The above solution uses a recursive approach to solve the problem. However, the following solution
# uses a stack to solve the problem. The time complexity of the following solution is O(n), where n is the
# number of characters in the string.
def separate_paren_groups_stack(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups_stack('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    res = []
    stack = []
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            stack.append(i)
        elif paren_string[i] == ')':
            if not stack:
                res.append(paren_string[i])
                continue
            else:
                stack.pop()
                if stack:
                    res