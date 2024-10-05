Here is a Python solution for the problem:

```
def separateParenGroups(paren_string):
    stack = []
    groups = []
    group = ''
    for char in paren_string:
        if char == '(':
            stack.append(char)
            group += char
        elif char == ')':
            if stack:
                stack.pop()
                group += char
                if not stack:
                    groups.append(group)
                    group = ''
            else:
                return []  # invalid parentheses
    if stack:
        return []  # invalid parentheses
    return groups

print(separateParenGroups('( ) (( )) (( )( ))'))
```

This code uses a stack to keep track of the parentheses. When it encounters an open parenthesis, it adds it to the stack and the current group. When it encounters a close parenthesis, it removes the corresponding open parenthesis from the stack and adds it to the current group. When the stack is empty (i.e., the current group is complete), it adds the current group to the list of groups and resets the current group. If the stack is not empty at the end of the input string, it means that there are unmatched open parentheses, so it returns an empty list. Otherwise, it returns the list of groups.