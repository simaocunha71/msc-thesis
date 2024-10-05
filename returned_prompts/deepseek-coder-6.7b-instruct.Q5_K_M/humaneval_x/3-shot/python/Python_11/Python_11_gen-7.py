    result = []
    for x, y in zip(a, b):
        result.append(str(int(x) ^ int(y)))
    return "".join(result)


