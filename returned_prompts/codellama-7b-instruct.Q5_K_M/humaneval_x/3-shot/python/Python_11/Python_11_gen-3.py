    result = ''
    for i, j in zip(a, b):
        if i == j:
            result += '0'
        else:
            result += '1'

    return result


