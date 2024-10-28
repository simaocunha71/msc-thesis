Here is the Python code for the problem:

```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    paren_string = paren_string.replace(" ","")  # Remove spaces
    stack = []  # Stack to store parentheses groups
    start = 0  # Start index of current group
    groups = []  # List to store separate groups

    for i, char in enumerate(paren_string):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if not stack:
                start = i + 1
            else:
                stack.pop()
                if not stack:
                    groups.append(paren_string[start:i+1])
    return groups
```

This code works by iterating over the input string and pushing indices of opening parentheses onto the stack. When it encounters a closing parenthesis, it pops the last index from the stack. If the stack becomes empty, it means we've found a group of parentheses. It then slices the string from the start index to the current index (inclusive) to get the group of parentheses and appends it to the groups list.

The time complexity of this code is O(n), where n is the length of the input string, because it iterates over the string once. The space complexity is also O(n), because in the worst case (when all parentheses are balanced and nested), the stack will store all indices of opening parentheses.

I hope this helps you understand how to solve this problem. Let me know if you have any other questions.


































































































































