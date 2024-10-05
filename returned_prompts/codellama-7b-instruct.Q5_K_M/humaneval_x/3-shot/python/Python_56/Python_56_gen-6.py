    opening = "<"
    closing = ">"
    count_opening = 0
    count_closing = 0

    for c in brackets:
        if c == opening:
            count_opening += 1
        elif c == closing:
            count_closing += 1

    return count_opening == count_closing


