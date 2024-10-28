from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    parens = [0]
    for c in paren_string:
        if c == "(":
            parens.append(parens[-1] + 1)
        elif c == ")":
            parens[-1] = parens[-2]
            parens.pop()
    return [max(parens)] + [max(parens[:i], parens[i:]) for i in range(1, len(parens))]
