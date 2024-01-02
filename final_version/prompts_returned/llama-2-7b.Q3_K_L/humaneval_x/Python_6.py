from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    if len(paren_string) == 0:
        return []

    # Input a string into the following function.
    def convert_to_list(n: str):
        return n[:-1].split(' ')

    # The function will return a list of groups, each of which is represented by '(', ')', or ' '.
    # For example, '(()())' represents a single group containing nested '(' and ')'s.
    def parse_input(input_string: str):
        return convert_to_list(input_string)

    groups = parse_input(paren_string[1:-1])  # Split on spaces to get the groups in the string.
    max_level = 0
    for group in groups:
        if len(group) == 2 and ')' in group[:-2]:
            level = group[-2]
            if level != '*':
                if level > max_level:
                    max_level = level
    return [max_level] + [1, 3, 1000 if groups[0][0] == '(' else len(groups[0]) - 1, 2]


if __name__ == "__main__":
    print(parse_nested_parens("(()()) ((())) () ((()()()))"))
