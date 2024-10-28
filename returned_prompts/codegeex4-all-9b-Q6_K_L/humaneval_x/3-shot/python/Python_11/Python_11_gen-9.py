    result = []
    for c1, c2 in zip(a, b):
        if c1 == c2:
            result.append('0')
        else:
            result.append('1')

    return ''.join(result)

