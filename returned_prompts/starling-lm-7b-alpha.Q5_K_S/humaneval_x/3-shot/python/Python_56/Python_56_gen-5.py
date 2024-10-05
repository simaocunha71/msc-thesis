    opening_brackets = 0
    closing_brackets = 0
    for c in brackets:
        if c == "<":
            opening_brackets += 1
        elif c == ">":
            closing_brackets += 1

    if opening_brackets != closing_brackets:
        return False

    opening_brackets = 0
    closing_brackets = 0
    for c in brackets[::-1]:
        if c == "<":
            closing_brackets += 1
        elif c == ">":
            opening_brackets += 1

    if opening_brackets != closing_brackets:
        return False

    return True


