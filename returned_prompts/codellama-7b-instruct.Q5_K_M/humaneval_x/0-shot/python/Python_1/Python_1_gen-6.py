from collections import deque


def separate_paren_groups(paren_string):
    stack = deque()
    groups = []
    for char in paren_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            stack.pop()
        if not stack:
            groups.append(paren_string[stack.index('('):])
    return groups
