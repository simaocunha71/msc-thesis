    result = ''
    for char_a, char_b in zip(a, b):
        result += str(int(char_a) ^ int(char_b))

    return result


