    opening_brackets = []
    closing_brackets = []

    for bracket in brackets:
        if bracket == "<":
            opening_brackets.append(bracket)
        if bracket == ">":
            if len(opening_brackets) == 0:
                return False
            else:
                opening_brackets.pop()

    if len(opening_brackets) == 0:
        return True
    else:
        return False


