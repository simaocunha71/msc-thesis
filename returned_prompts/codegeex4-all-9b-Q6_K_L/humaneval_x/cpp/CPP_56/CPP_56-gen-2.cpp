def correct_bracketing(brackets):
    """brackets is a string of '<' and '>'.
    return true if every opening bracket has a corresponding closing bracket.
    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    while brackets.count("<") != brackets.count(">"):
        brackets = brackets.replace("<>", "")
    return brackets.count("<") == brackets.count(">")

print(correct_bracketing("<"))
print(correct_bracketing("<>"))
print(correct_bracketing("<<><>>"))
print(correct_bracketing("><<>"))