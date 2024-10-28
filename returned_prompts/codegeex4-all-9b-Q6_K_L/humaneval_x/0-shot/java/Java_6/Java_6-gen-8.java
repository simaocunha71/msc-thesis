Here is a Python solution using a stack to track the levels of nesting:

```python
def parseNestedParens(paren_string):
    groups = paren_string.split(' ')
    result = []
    for group in groups:
        stack = []
        max_depth = 0
        for char in group:
            if char == '(':
                stack.append(char)
                max_depth = max(max_depth, len(stack))
            elif char == ')':
                stack.pop()
        result.append(max_depth)
    return result

print(parseNestedParens("(()()) ((())) () ((())()())"))  # Output: [2, 3, 1, 3]
```

In this code, for each group in the input string, we iterate over the characters in the group. If we encounter an open parenthesis '(', we push it onto the stack and update the maximum depth. If we encounter a close parenthesis ')', we pop the stack. After iterating over all the characters in the group, we add the maximum depth to the result list. Finally, we return the result list.