```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    groups = paren_string.split(' ')
    results = []

    for group in groups:
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

This code works by splitting the input string on spaces to get each group of parentheses. Then for each group, it traverses the characters. For each opening parenthesis, it increments the current depth, and if the current depth is greater than the max depth, it updates the max depth. For each closing parenthesis, it decrements the current depth. The maximum depth is the maximum level of nesting in the parentheses group. This is appended to the results list and returned at the end.

This solution assumes that the input string is well-formed and only contains parentheses and spaces. If this is not the case, additional error checking would be needed.

Also note that this solution assumes that the depth of parentheses is being measured based on the number of open parentheses, not the content within them. If this is not the case, the depth calculation would need to be adjusted accordingly.

Finally, this solution assumes that the maximum depth of nested parentheses is being measured as a single character '(' being counted for each level of nesting. If this is not the case, the calculation would need to be adjusted accordingly.

So, the depth of nesting is being calculated based on the number of open parentheses, and it's not considering the content within the parentheses.

In the given example, the depth of nesting for '(()())' is 2, for '((()))' is 3, for '()' is 1, and for '((())()())' is 3.
