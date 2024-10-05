    result = ""
    for c in s:
        if c.isalpha():
            result += c.swapcase()
        else:
            result += c

    if result.isalpha():
        return result[::-1]
    else:
        return result

