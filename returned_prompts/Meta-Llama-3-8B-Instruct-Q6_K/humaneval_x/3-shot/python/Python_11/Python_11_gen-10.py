    result = ''
    for char_a, char_b in zip(a, b):
        if char_a == char_b:
            result += '0'
        else:
            result += '1'

    return result


