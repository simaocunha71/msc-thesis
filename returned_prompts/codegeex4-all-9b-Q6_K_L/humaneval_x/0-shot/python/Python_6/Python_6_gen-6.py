Here's one way to do it:

```python
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    groups = paren_string.split()
    result = []
    for group in groups:
        max_depth = 0
        current_depth = 0
        for char in group:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
        result.append(max_depth)
    return result
```

This function first splits the input string into individual groups using the `split()` method. It then iterates over each group and calculates the maximum depth of nesting of parentheses by keeping track of the current depth and updating the maximum depth whenever a new maximum is found. Finally, it appends the maximum depth to the result list and returns the result list.