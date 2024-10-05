from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    result = []

    for char in paren_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            group = []
            while stack and stack[-1] != '(':
                group.append(stack.pop())
            if stack:
                stack.pop()
            group = ''.join(group)
            result.append(group[::-1])

    return result


print(separate_paren_groups('( ) (( )) (( )( ))'))