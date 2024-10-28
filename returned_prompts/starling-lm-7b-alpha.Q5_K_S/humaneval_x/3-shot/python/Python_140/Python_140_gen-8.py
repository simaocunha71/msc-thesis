    result = []
    consecutive_spaces = False

    for c in text:
        if c == ' ':
            if consecutive_spaces:
                result.append('-')
            else:
                result.append('_')
                consecutive_spaces = True
        else:
            result.append(c)
            consecutive_spaces = False

    return ''.join(result)


