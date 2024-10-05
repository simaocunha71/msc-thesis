    result = ""
    for a, b in zip(a, b):
        if a == b:
            result += '0'
        else:
            result += '1'
    return result


