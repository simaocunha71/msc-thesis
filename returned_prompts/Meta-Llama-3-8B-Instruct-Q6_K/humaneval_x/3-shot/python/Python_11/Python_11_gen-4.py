    result = ''
    for idx, c in enumerate(zip(a, b)):
        if c[0] != c[1]:
            result += '1'
        else:
            result += '0'

    return result


