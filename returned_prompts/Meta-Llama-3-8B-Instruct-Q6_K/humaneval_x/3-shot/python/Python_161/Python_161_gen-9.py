    result = ""
    for c in s:
        if c.isalpha():
            result += c.swapcase()
        else:
            result += c
    return result if result.isalpha() else result[::-1]  # reverse the string if no letters are found


