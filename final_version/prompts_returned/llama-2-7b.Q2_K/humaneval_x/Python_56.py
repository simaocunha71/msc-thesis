

def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """

    open_brackets = set()  # type: ignore[set] # noqa: E501
    close_brackets = set()  # type: ignore[set] # noqa: E501

    for idx, ch in enumerate(brackets):
        if ch == ">":
            open_brackets.add(idx)
        elif ch == "<":
            close_brackets.add(idx + 1)
        else:
            raise ValueError("Invalid bracket type.")

    while True:
        idx = next(open_brackets, None)
        if not (idx is None):
            open_brackets.remove(idx)
            break

    return (close_brackets - open_brackets).count() == 0
