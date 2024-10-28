Here is a Python solution to the problem:

```Python
def separateParenGroups(paren_string):
    result = []
    stack = []
    temp = ''
    
    for char in paren_string:
        if char == ' ':
            continue
        if char == '(':
            stack.append(char)
            temp += char
        elif char == ')':
            if stack:
                stack.pop()
                temp += char
                if not stack:
                    result.append(temp)
                    temp = ''
            else:
                return 'Invalid parentheses'
    
    if stack:
        return 'Invalid parentheses'
    
    return result
```

This function iterates over the input string and separates the parentheses into groups. When it encounters an open parenthesis, it pushes it onto the stack and adds it to the temporary string. When it encounters a close parenthesis, it pops the stack and adds it to the temporary string. If the stack is empty when it encounters a close parenthesis, it means that there's an unbalanced close parenthesis, so it returns 'Invalid parentheses'. If the stack is not empty at the end, it means that there's an unbalanced open parenthesis, so it also returns 'Invalid parentheses'. If the function finishes iterating over the string without encountering any errors, it adds the temporary string to the result list and resets the temporary string. Finally, it returns the list of separated parentheses groups.