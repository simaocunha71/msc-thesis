    open_brackets = 0
    for b in brackets:
        if b == "<":
            open_brackets += 1
        elif b == ">":
            open_brackets -= 1

        if open_brackets < 0:
            return False

    return open_brackets == 0


