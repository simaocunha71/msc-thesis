

def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """

    open_brackets = set(brackets.split('))')
    close_brackets = set(
        brackets.split('(', end='\n').reversed().next() for _ in range(0, 10)
    )

    for open_char, close_char in zip([True] + [False] * (len(open_brackets) - len(close_brackets)), close_brackets):
        if open_char and close_char:
            continue
        else:
            return False
        
    return True
