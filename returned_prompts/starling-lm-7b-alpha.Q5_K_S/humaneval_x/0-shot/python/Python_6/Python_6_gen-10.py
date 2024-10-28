    def parse_nested_parens(paren_string: str) -> List[int]:
        levels = []
        for char in paren_string:
            if char == '(':
                levels.append(levels[-1] + 1)
            elif char == ')':
                levels.append(levels[-1] - 1)
        return levels


# print(parse_nested_parens('(()()) ((())) () ((())()())'))  # [2, 3, 1, 3]
# print(parse_nested_parens('(()(())))'))  # [2, 3, 2, 1, 2]


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def parse_nested_parens_helper(paren_string: str) -> List[int]:
        levels = []
        for char in paren_string:
            if char == '(':
                levels.append(levels[-1] + 1)
            elif char == ')':
                levels.append(levels[-1] - 1)
        return levels
    return parse_nested_parens_helper(paren_string)


# print(parse_nested_parens('(()()) ((())) () ((())()())'))  # [2, 3, 1, 3]
# print(parse_nested_parens('(()(())))'))  # [2, 3, 2, 1, 2]


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of