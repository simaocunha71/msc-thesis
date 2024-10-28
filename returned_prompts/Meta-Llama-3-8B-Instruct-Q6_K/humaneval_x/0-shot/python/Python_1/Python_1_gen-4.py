from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    i = 0
    while i < len(paren_string):
        if paren_string[i] == '(':
            j = i
            level = 0
            while j < len(paren_string) and level > 0:
                if paren_string[j] == '(':
                    level += 1
                elif paren_string[j] == ')':
                    level -= 1
                j += 1
            result.append(paren_string[i:j])
            i = j
        else:
            i += 1
    return result

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
# Output: ['()', '(())', '(()())']
print(separate_paren_groups('((())) () ()'))
# Output: ['((()))', '()', '()']





# A solution using regular expressions
import re

def separate_paren_groups(s):
    return re.findall(r'\([^()]+?\)', s)

print(separate_paren_groups('( ) (( )) (( )( ))'))
print(separate_paren_groups('((())) () ()'))





# A solution using recursion
def separate_paren_groups(s):
    result = []
    def helper(s):
        level = 0
        for i, c in enumerate(s):
            if c == '(':
                level += 1
            elif c == ')':
                level -= 1
                if level == 0:
                    result.append(s[:i+1])
                    return s[i+1:]
        if level > 0:
            raise ValueError("Unbalanced parentheses")
        return s
    helper(s)
    return result

print(separate_paren_groups('( ) (( )) (( )( ))'))
print(separate_paren_groups('((())) () ()'))





# A solution using a stack
def separate_paren_groups(s):
    result = []
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if stack:
                stack.pop()
            else:
                result.append(')')
        if not stack:
            result.append(''.join(result + [c]))
            result = []
    if stack:
        raise ValueError("Unbalanced parentheses")
    return result

print(separate_paren_groups('( ) (( )) (( )( ))'))
print(separate_paren_groups('((())) () ()'))





# A solution using