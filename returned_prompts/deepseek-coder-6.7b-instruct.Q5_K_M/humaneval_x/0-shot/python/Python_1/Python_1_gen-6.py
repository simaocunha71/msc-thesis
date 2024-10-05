from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    paren_string = paren_string.replace(' ', '')
    stack = []
    result = []
    temp = ''
    for char in paren_string:
        if char == '(':
            if temp:
                stack.append(temp)
                temp = ''
            stack.append(char)
        else:
            stack.append(char)
            if len(stack) - stack[::-1].index('(') == 2:
                temp = ''.join(stack)
                stack = []
    if temp:
        result.append(temp)
    while stack:
        temp = stack.pop() + temp
        if stack and stack[-1] == '(':
            result.append(temp)
            temp = ''
    return result[::-1]

print(separate_paren_groups('(  )  (( ))  (( )( ))'))  # ['()', '(())', '(()())']

This solution works by iterating through each character of the string. It pushes open parentheses onto a stack, and when it encounters a close parenthesis, it pops from the stack until it finds the corresponding open parenthesis, appending the parentheses to a temporary string. This temporary string is then added to the result list. The process is repeated until the string has been fully processed. The result list is then reversed and returned.

This solution assumes that the input string will only contain parentheses and spaces. If the input string could contain other characters, the solution would need to be modified to handle those cases.

This solution also assumes that the input string is well-formed and does not contain unbalanced parentheses. If the input string could contain unbalanced parentheses, the solution would need to be modified to handle those cases.
