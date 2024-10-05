    opening_brackets = []
    for bracket in brackets:
        if bracket == '(':
            opening_brackets.append(bracket)
        elif bracket == ')' and opening_brackets:
            opening_brackets.pop()
        else:
            return False
    return len(opening_brackets) == 0


