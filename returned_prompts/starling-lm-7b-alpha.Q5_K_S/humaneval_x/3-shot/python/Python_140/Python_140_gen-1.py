    result = ""
    previous_space = False
    for c in text:
        if c == ' ':
            if not previous_space:
                result += '_'
            previous_space = True
        else:
            result += c
            previous_space = False
    if previous_space:
        result += '-'
    return result


