```python
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    def parse_group(group):
        stack = []
        max_depth = 0
        current_depth = 0
        for char in group:
            if char == '(':
                stack.append(char)
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                stack.pop()
                current_depth -= 1
        return max_depth

    return [parse_group(group) for group in paren_string.split(' ') if group]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
```