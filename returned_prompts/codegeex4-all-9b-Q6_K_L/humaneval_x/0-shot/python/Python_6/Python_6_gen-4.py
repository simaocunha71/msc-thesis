```python
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    def get_depth(s: str) -> int:
        """ Get the maximum depth of nesting of parentheses in a string s. """
        depth = 0
        max_depth = 0
        for char in s:
            if char == '(':
                depth += 1
                max_depth = max(depth, max_depth)
            elif char == ')':
                depth -= 1
        return max_depth

    groups = paren_string.split(' ')
    return [get_depth(group) for group in groups]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
```
