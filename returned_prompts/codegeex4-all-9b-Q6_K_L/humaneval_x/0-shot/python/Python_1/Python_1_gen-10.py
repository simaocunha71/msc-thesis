from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    result = []

    for char in paren_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
                if not stack:
                    result.append(''.join(paren_string.split()[i] for i in range(start, idx + 1)))
            else:
                start = idx + 1

    return result

print(separate_paren_groups('( ) (( )) (( )( ))'))