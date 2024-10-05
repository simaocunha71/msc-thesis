    result = ''
    for a, b in zip(a, b):
        result += str(int(a) ^ int(b))
    return result


