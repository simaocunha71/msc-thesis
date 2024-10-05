    result = []
    for a, b in zip(a, b):
        result.append(str(int(a) ^ int(b)))
    return ''.join(result)


