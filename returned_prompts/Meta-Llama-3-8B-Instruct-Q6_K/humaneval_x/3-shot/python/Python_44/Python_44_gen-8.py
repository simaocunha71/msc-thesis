    convertString = "0123456789"
    result = ""

    while x > 0:
        result = convertString[x % base] + result
        x = x // base

    return result


