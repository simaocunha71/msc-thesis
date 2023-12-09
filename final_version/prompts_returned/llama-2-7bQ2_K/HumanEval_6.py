from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    groups = paren_string.split(" ")
    level: int = 0  # Current level of nesting
    output_list: List[int] = []
    nested_levels: List[int] = [level]
    for paren in groups:
        if paren == "()":
            pass
        elif paren == "{}:":
            level += 1
            nested_levels.append(level)
        else:
            output_list.append(nested_levels[-1] - level + 1)
    return output_list

if __name__ == "__main__":
    print("Hello World!")