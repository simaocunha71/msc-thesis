    opening_brackets_count = 0
    closing_brackets_count = 0

    for c in brackets:
        if c == "(":
            opening_brackets_count += 1
        elif c == ")":
            closing_brackets_count += 1
        else:
            raise ValueError("Invalid bracket")

    return opening_brackets_count == closing_brackets_count


