```python
def parse_nested_parens(paren_string: str) -> List[int]:
    groups = paren_string.split()
    result = []
    for group in groups:
        stack = []
        max_depth = 0
        for char in group:
            if char == '(':
                stack.append(char)
                if len(stack) > max_depth:
                    max_depth = len(stack)
            elif char == ')':
                stack.pop()
        result.append(max_depth)
    return result
```

This solution works by iterating over each character in the parentheses group. If a '(' is encountered, it is added to a stack, and if a ')' is encountered, it is removed from the stack. The length of the stack at any point represents the current level of nesting, and if this length is greater than the maximum depth seen so far, it is updated. This process is repeated for each group of parentheses, and the maximum depth for each group is stored in the result list.

This solution assumes that the input string is well-formed and contains balanced parentheses. If this is not the case, additional error checking may be necessary.

Also, this solution assumes that the groups of parentheses are separated by spaces. If they are separated by other characters, the split method should be adjusted accordingly.
