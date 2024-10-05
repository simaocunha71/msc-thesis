    result = False
    open_brackets = 0
    for c in string:
        if c == '[':
            open_brackets += 1
        else:
            open_brackets -= 1

        if open_brackets < 0:
            result = True
            break

    return result


