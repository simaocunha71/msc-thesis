    result = []
    for i, j in zip(a, b):
        if i == j:
            result.append('0')
        else:
            result.append('1')

    return ''.join(result)


