    result = ""
    for char in text:
        if char == ' ':
            if result[-1] == ' ':
                result += '-'
            else:
                result += '_'
        else:
            result += char
    return result


