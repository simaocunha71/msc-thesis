def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    groups = []
    paren_string = paren_string.replace(' ', '')
    for char in paren_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
                if not stack:
                    groups.append(''.join(paren_string.split(')')[0].split('(')))
                    paren_string = paren_string.split(')')[1]
            else:
                break
    return groups

print(separate_paren_groups('( ) (( )) (( )( ))'))