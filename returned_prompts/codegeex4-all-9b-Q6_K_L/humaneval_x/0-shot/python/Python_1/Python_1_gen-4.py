from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    paren_string = paren_string.replace(' ', '')
    result = []
    stack = []
    for char in paren_string:
        if char == '(':
            stack.append('(')
        elif char == ')':
            group = ''
            while stack and stack[-1] == '(':
                group = '(' + group
                stack.pop()
            if stack:
                stack[-1] += group
            else:
                result.append(group)
    return result


# Test cases
assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
assert separate_paren_groups('(())(())') == ['(())', '(())']
assert separate_paren_groups('((()))') == ['((()))']
assert separate_paren_groups('()()()') == ['()', '()', '()']
assert separate_paren_groups('()()()()') == ['()', '()', '()', '()']
assert separate_paren_groups('((()))((()))') == ['((()))', '((()))']
assert separate_paren_groups('((()))((()))((()))') == ['((()))', '((()))', '((()))']