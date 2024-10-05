    result = []
    consecutive_spaces = 0
    for c in text:
        if c == ' ':
            consecutive_spaces += 1
            if consecutive_spaces > 2:
                result.append('-')
        else:
            consecutive_spaces = 0
            result.append(c)

    return ''.join(result)


