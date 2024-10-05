from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    groups = paren_string.split(' ')
    results = []
    for group in groups:
        stack = []
        max_depth = 0
        current_depth = 0
        for char in group:
            if char == '(':
                stack.append(char)
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                stack.pop()
                current_depth -= 1
        results.append(max_depth)
    return results

if __name__ == "__main__":
    import doctest
    doctest.testmod()

This solution uses a stack to track the depth of nesting for each group of parentheses. It iterates through each character in each group, incrementing the depth when it encounters an opening parenthesis and decrementing it when it encounters a closing parenthesis. It keeps track of the maximum depth encountered for each group and appends it to the results list. The function then returns the results list.