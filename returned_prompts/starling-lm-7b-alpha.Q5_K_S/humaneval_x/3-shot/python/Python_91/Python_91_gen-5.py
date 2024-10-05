    result = 0
    prev_letter = ''
    for c in S:
        if c == '.' or c == '?' or c == '!':
            if prev_letter == 'I' or prev_letter == 'i':
                result += 1
            prev_letter = ''
        elif c == ' ' and prev_letter == 'I' or prev_letter == 'i':
            result += 1
        else:
            prev_letter = c
    return result


