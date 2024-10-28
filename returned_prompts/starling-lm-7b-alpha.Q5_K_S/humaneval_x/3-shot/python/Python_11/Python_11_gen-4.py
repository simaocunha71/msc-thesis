    result = []
    for c1, c2 in zip(a, b):
        if c1 == '0' and c2 == '0':
            result.append('0')
        elif c1 == '1' and c2 == '1':
            result.append('0')
        elif c1 == '0' and c2 == '1':
            result.append('1')
        elif c1 == '1' and c2 == '0':
            result.append('1')

    return ''.join(result)


