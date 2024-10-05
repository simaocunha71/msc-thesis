    opening_brackets = "("<
    closing_brackets = ">)">"
    opening_count = 0
    closing_count = 0

    for bracket in brackets:
        if bracket in opening_brackets:
            opening_count += 1
        elif bracket in closing_brackets:
            closing_count += 1

    return opening_count == closing_count


