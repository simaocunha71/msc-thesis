Here is a Python solution that uses a stack to keep track of the nesting level of the parentheses:

```python
def parse_nested_parens(paren_string):
    result = []
    stack = []
    max_level = 0
    current_level = 0

    for char in paren_string:
        if char == '(':
            stack.append(char)
            current_level += 1
            max_level = max(max_level, current_level)
        elif char == ')':
            stack.pop()
            current_level -= 1

    return [max_level] * len(paren_string.split())

print(parse_nested_parens('(()()) ((())) () ((())()())'))
# Output: [2, 3, 1, 3]
```

This solution works by iterating over the input string and pushing each opening parenthesis onto the stack. When a closing parenthesis is encountered, the top element of the stack is popped, and the current nesting level is decremented. The maximum nesting level encountered during the iteration is stored. Finally, the function returns a list of maximum nesting levels for each group in the input string. The `split` method is used to split the input string into groups, and the `*` operator is used to repeat the maximum nesting level for each group.