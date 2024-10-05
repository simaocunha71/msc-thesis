    result = ''
    for c1, c2 in zip(a, b):
        if c1 == c2:
            result += '0'
        else:
            result += '1'

    return result


