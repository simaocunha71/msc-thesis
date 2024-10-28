Here is a Python solution for your problem. This function uses a stack to separate the groups of parentheses. It iterates over the string, pushing opening parentheses onto the stack and popping them off when it encounters a closing parenthesis. When the stack is empty, it means that we have found a separate group, so we add it to our result list.

```python
def separateParenGroups(paren_string):
    stack = []
    groups = []
    current_group = ""
    
    for char in paren_string:
        if char == "(":
            stack.append(char)
            current_group += char
        elif char == ")":
            if stack:
                stack.pop()
                current_group += char
                if not stack:
                    groups.append(current_group)
                    current_group = ""
            else:
                return "Invalid parentheses"
    
    if stack:
        return "Invalid parentheses"
    
    return groups

print(separateParenGroups('( ) (( )) (( )( ))'))
```

When you run this function with the input `( ) (( )) (( )( ))`, it returns `['()', '(())', '(()())']`, as expected. The function correctly separates the groups of parentheses and returns them as a list of strings. It also handles the case where the input string is invalid (i.e., it contains unmatched parentheses) by returning an error message.