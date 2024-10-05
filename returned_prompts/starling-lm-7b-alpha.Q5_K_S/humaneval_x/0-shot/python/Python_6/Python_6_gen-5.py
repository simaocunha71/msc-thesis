    def _count_open_parens(s):
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
        return count

    levels = []
    for group in paren_string.split():
        levels.append(_count_open_parens(group))
    return levels

#from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    def _count_open_parens(s):
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
        return count

    levels = []
    for group in paren_string.split():
        levels.append(_count_open_parens(group))
    return levels


# Run tests
import doctest
if __name__ == "__main__":
    doctest.testmod()
























# Testing
#from typing import List


#def parse_nested_parens(paren_string: str) -> List[int]:
#    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
#    For each of the group, output the deepest level of nesting of parentheses.
#    E.g. (()()) has maximum two levels of nesting while ((())) has three.
#
#    >>> parse_nested_parens('(()()) ((())) () ((())()())')
#    [2, 3, 