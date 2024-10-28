Here is a Python solution that uses a stack to keep track of the opening parentheses and a loop to iterate over the string:

```python
def separateParenGroups(paren_string):
    result = []
    stack = []
    current_group = ''
    
    for char in paren_string:
        if char == '(':
            stack.append(char)
            current_group += char
        elif char == ')':
            stack.pop()
            current_group += char
            if not stack:
                result.append(current_group)
                current_group = ''
    
    return result
```

This function initializes an empty result list, an empty stack, and an empty current group string. It then iterates over the input string, pushing opening parentheses onto the stack and appending them to the current group string. When it encounters a closing parenthesis, it pops the opening parenthesis from the stack and appends the closing parenthesis to the current group string. If the stack is empty after processing a closing parenthesis, it means that the current group has been fully processed, so it is added to the result list and reset. Finally, the function returns the list of separated groups.