    result = []
    for char_a, char_b in zip(a, b):
        if char_a == char_b:
            result.append('0')
        else:
            result.append('1')

    return ''.join(result)


