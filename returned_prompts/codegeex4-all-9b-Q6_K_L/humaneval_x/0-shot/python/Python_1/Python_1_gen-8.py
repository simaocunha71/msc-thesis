```python
from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    paren_string = paren_string.replace(" ", "")
    stack = []
    groups = []
    current_group = ""
    for char in paren_string:
        if char == "(":
            stack.append(char)
            current_group += char
        elif char == ")":
            stack.pop()
            current_group += char
            if not stack:
                groups.append(current_group)
                current_group = ""
    return groups
```

The function `separate_paren_groups` takes a string containing multiple groups of nested parentheses as input. It removes all spaces from the input string and initializes an empty stack and list to keep track of the current group of parentheses and the list of all groups. 

For each character in the input string, if the character is an open parenthesis, it is added to the stack and the current group. If the character is a closing parenthesis, it is removed from the stack and the current group. If the stack is empty after adding the closing parenthesis, it means a group has been completed and it is added to the list of groups. 

Finally, the function returns the list of all groups.