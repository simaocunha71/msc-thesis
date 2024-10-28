    result = []
    spaces = False
    consecutive_spaces = False
    for c in text:
        if c == " ":
            if consecutive_spaces:
                result.append('-')
            else:
                result.append('_')
            consecutive_spaces = True
        elif consecutive_spaces:
            consecutive_spaces = False
            result.append('-')
        else:
            result.append(c)
    return "".join(result)


