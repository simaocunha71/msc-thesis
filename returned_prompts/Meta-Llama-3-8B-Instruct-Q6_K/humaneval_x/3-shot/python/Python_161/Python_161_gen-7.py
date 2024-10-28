    result = ""
    for c in s:
        if c.isalpha():
            result += c.swapcase()
        else:
            result += c
    if not result.isalpha():
        result = result[::-1]
    return result
# or
    return s.swapcase() if s.isalpha() else s[::-1] if not s.isalpha() else s


