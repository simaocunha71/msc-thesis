```python
def parse_nested_parens(paren_string: str) -> List[int]:
    group_list = paren_string.split(' ')
    results = []
    for group in group_list:
        max_depth = 0
        current_depth = 0
        for char in group:
            if char == '(':
                current_depth += 1
                if current_depth > max_depth:
                    max_depth = current_depth
            elif char == ')':
                current_depth -= 1
        results.append(max_depth)
    return results
```

This solution works by iterating over each group of parentheses and calculating the maximum depth of nesting. The depth is increased when an opening parenthesis is found and decreased when a closing parenthesis is found. The maximum depth is updated whenever the current depth is greater than the maximum depth.

The function splits the input string into a list of groups using the split function, then iterates over each group. For each group, it initializes the maximum depth and current depth to 0, then iterates over each character in the group. If the character is an opening parenthesis, it increments the current depth and updates the maximum depth if necessary. If the character is a closing parenthesis, it decrements the current depth. Finally, it appends the maximum depth to the results list.

Finally, it returns the results list.

This solution has a time complexity of O(n), where n is the total number of characters in the input string. This is because it makes a single pass over the input string for each group.

The space complexity of the solution is O(m), where m is the number of groups in the input string. This is because it stores the results for each group in a list.

This solution assumes that the input string is well-formed and contains only parentheses and spaces. If this is not the case, additional error checking or input validation may be necessary.

Note: This solution assumes that the input string is well-formed and contains only parentheses and spaces. If this is not the case, additional error checking or input validation may be necessary.

Note: This solution assumes that the input string is well-formed and contains only parentheses and spaces. If this is not the case, additional error