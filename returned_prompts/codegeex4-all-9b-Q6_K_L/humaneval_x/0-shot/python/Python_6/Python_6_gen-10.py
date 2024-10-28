```python
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    def get_depth(paren_group: str) -> int:
        depth = 0
        max_depth = 0
        for char in paren_group:
            if char == '(':
                depth += 1
                max_depth = max(depth, max_depth)
            elif char == ')':
                depth -= 1
        return max_depth

    return [get_depth(group) for group in paren_string.split(' ') if group]

```
