    levels = []
    for paren_group in paren_string.split():
        level = 0
        for char in paren_group:
            if char == "(":
                level += 1
            elif char == ")":
                level -= 1
            if level > levels[-1]:
                levels.append(level)
    return levels



























# def parse_nested_parens(paren_string: str) -> List[int]:
#     """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
#     For each of the group, output the deepest level of nesting of parentheses.
#     E.g. (()()) has maximum two levels of nesting while ((())) has three.

#     >>> parse_nested_parens('(()()) ((())) () ((())()())')
#     [2, 3, 1, 3]
#     """

#     levels = []
#     for paren_group in paren_string.split():
#         curr_level = 0
#         for char in paren_group:
#             if char == "(":
#                 curr_level += 1
#             elif char == ")":
#                 curr_level -= 1
#             if curr_level > levels[-1]:
#                 levels.append(curr_level)
#     return levels
































# def parse_nested_parens(paren_string: str) -> List[int]:
#     """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
#     For each of the group, output the deepest level of nesting of parentheses.
#     E.g. (()()) has maximum two levels of nesting while ((())) has three.

#     >>> parse_nested_parens('(()()) ((())) () ((())()())')
#     [2, 3, 1, 3]
#     """
