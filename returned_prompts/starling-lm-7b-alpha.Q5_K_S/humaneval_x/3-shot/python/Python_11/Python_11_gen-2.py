    result = ""
    for a_char, b_char in zip(a, b):
        if a_char == '1' and b_char == '1':
            result += '0'
        else:
            result += '1'

    return result


