    open_brackets = []
    for bracket in brackets:
        if bracket == "(":
            open_brackets.append(bracket)
        elif bracket == ")":
            if len(open_brackets) == 0:
                return False
            open_brackets.pop()

    if len(open_brackets) == 0:
        return True

    return False


