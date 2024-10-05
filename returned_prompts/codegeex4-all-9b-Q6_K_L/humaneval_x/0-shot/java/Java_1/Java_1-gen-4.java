Here is a Python solution that uses a stack to keep track of the parentheses:

```python
def separateParenGroups(paren_string):
    paren_string = paren_string.replace(' ', '')
    groups = []
    stack = []
    current_group = ""
    for char in paren_string:
        if char == '(':
            stack.append(char)
            current_group += char
        elif char == ')':
            stack.pop()
            current_group += char
            if not stack:
                groups.append(current_group)
                current_group = ""
    return groups

print(separateParenGroups("( ) (( )) (( )( ))"))  # ["()", "(())", "(()())"]
```

In this solution, we iterate over each character in the input string. If the character is an open parenthesis '(', we add it to the stack and to the current group. If the character is a close parenthesis ')', we remove an open parenthesis from the stack and add the close parenthesis to the current group. If the stack is empty (i.e., we've found a complete group), we add the current group to the list of groups and start a new group. Finally, we return the list of groups.