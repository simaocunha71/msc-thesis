    result = ''
    for c1, c2 in zip(a, b):
        if c1 != c2:
            result += '1'
        else:
            result += '0'
    return result


