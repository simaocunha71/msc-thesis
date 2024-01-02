from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    result = []
    current_group = ''
    prev_position = 0
    for index, char in enumerate(paren_string):
        if char == '(' or char == ')':
            current_group += f'({char})'
            continue

        if char == ')':
            result.append(current_group)
            current_group = ''
            continue

        if index - 1 < prev_position:
            result.append(current_group)
            current_group = ''
            continue

        prev_position = index + 1

    if current_group != '':
        result.append(current_group)

    return result