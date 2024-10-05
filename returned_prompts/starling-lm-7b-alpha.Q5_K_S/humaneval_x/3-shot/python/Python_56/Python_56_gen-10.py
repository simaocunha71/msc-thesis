    opening_brackets = "()[]{}<>"
    opening_count = 0
    closing_count = 0

    for bracket in brackets:
        if bracket in opening_brackets:
            opening_count += 1
        elif bracket in opening_brackets[::-1]:
            closing_count += 1
        else:
            opening_count = 0
            closing_count = 0
            break

    return opening_count == closing_count


