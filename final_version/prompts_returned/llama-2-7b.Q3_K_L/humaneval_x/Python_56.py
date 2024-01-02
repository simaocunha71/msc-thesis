

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
    
    brackets = set(brackets)
    for symbol in brackets: #for each character in the string
        brackets.remove(symbol)   #remove that character from brackets
        
    return len(brackets) == 0