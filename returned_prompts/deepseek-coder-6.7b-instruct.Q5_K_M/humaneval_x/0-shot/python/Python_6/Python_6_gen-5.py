```python
def parse_nested_parens(paren_string: str) -> List[int]:
    output = []
    groups = paren_string.split()
    for group in groups:
        count = 0
        max_count = 0
        for char in group:
            if char == '(':
                count += 1
            else:
                count -= 1
            max_count = max(max_count, count)
        output.append(max_count)
    return output
```

This solution works by iterating through each character in the string. If the character is an opening parenthesis, the count is increased by 1. If the character is a closing parenthesis, the count is decreased by 1. The maximum count is updated every time the count is updated. This maximum count gives us the deepest level of nesting for each group of parentheses.

The function splits the input string into groups separated by spaces and then processes each group in the same way. The results are stored in the output list which is returned at the end.

This solution assumes that the input string is well-formed and contains only parentheses and spaces. It does not handle invalid inputs.

The time complexity of this solution is O(n), where n is the total number of characters in the input string. The space complexity is O(m), where m is the number of groups in the input string.
