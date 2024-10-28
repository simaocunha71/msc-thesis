    result = []

    for c_a, c_b in zip(a, b):
        if c_a == c_b:
            result.append('0')
        else:
            result.append('1')

    return ''.join(result)


