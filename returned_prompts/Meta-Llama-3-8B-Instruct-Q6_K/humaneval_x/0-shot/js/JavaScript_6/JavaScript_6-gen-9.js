Here is a Python solution for your problem. This function iterates over each group of parentheses in the input string, and for each group, it counts the number of opening and closing parentheses, and the maximum depth of nesting is the minimum of these two counts.

```python
def parse_nested_parens(paren_string):
    result = []
    temp = []
    max_depth = 0
    for char in paren_string:
        if char == '(':
            temp.append(char)
            max_depth = max(max_depth, len(temp))
        elif char == ')':
            temp.pop()
            if not temp:
                result.append(max_depth)
                max_depth = 0
    return result
```

This function works by iterating over each character in the input string. If the character is an opening parenthesis, it is added to the temporary list, and the maximum depth is updated. If the character is a closing parenthesis, the temporary list is popped, and if the temporary list is now empty, it means that we have just finished processing a group of parentheses, and the maximum depth of this group is added to the result list. The maximum depth is then reset to 0. Finally, the function returns the result list.