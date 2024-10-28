    result = ""
    for c in s:
        if c.isalpha():
            result += c.swapcase()
        else:
            result += c
    if not result.isalpha():
        result = result[::-1]
    return result


