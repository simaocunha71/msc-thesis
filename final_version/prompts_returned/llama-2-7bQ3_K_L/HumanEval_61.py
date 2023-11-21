

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
    
    # open bracket counter
    opener = 0 

    # close bracket counter
    clooser = 0
        
    if brackets[0] == "(":
        opener +=1
    else:
        return False

    for i, ch in enumerate(brackets):
        # handle case where a "(", ")" is followed by another "(" or ")"
        # so you're not opening or closing bracketing at the wrong level
        if (ch == ")") and clooser != 0:
            return False
        
        elif ch == "(":
            opener +=1
            
        elif ch == ")":
            clooser +=1
            
    # check for extra closing bracket
    if clooser <= 2:
        return False
    
    # check for missing opening bracket
    if (opener < 2):
        return False

    return True

