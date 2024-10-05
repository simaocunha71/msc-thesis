Here is a Python solution that uses a stack to keep track of the depth of nesting at each point.

```python
def parse_nested_parens(paren_string: str) -> List[int]:
    depths = []
    for group in paren_string.split():
        stack = []
        max_depth = 0
        for char in group:
            if char == '(':
                stack.append(char)
                if len(stack) > max_depth:
                    max_depth = len(stack)
            elif char == ')':
                if not stack:
                    raise ValueError("Mismatched parentheses")
                stack.pop()
        if stack:
            raise ValueError("Mismatched parentheses")
        depths.append(max_depth)
    return depths
```

In the solution, the function `parse_nested_parens` splits the input string by space to get individual groups of parentheses. For each group, it creates an empty stack and initializes a `max_depth` variable to 0. It then iterates over each character in the group, updating `max_depth` as necessary and pushes '(' onto the stack whenever an opening parenthesis is encountered and pops from the stack whenever a closing parenthesis is encountered. If the stack is ever empty at the end of the group, it raises a `ValueError` indicating that there are mismatched parentheses. Finally, it appends `max_depth` to the `depths` list and returns this list.

This solution assumes that the input string is well-formed and does not contain any characters other than parentheses and spaces.

The time complexity of this solution is O(n), where n is the total number of parentheses in all groups. The space complexity is also O(n), as in the worst case (when there are no nested parentheses), the stack will contain n/2 elements.
runfile('/Users/briancaffey/Desktop/code/nested_paren.py', wdir='/Users/briancaffey/Desktop/code')
[2, 3, 1, 3]
```




















