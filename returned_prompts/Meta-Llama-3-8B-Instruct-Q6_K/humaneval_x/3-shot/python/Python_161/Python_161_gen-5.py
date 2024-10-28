    result = ""
    for c in s:
        if c.isalpha():
            result += c.swapcase()
        else:
            result += c
    if result.isalpha():
        result = result[::-1]
    return result


