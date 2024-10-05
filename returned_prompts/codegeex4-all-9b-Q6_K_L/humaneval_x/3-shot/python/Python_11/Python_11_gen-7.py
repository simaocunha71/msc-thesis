    result = []
    for c1, c2 in zip(a, b):
        result.append(str(int(c1) ^ int(c2)))

    return ''.join(result)

