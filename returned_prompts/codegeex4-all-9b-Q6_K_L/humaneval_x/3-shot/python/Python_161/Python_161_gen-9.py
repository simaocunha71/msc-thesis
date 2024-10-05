    result = ""
    for c in s:
        if c.isalpha():
            if c.isupper():
                result += c.lower()
            else:
                result += c.upper()
        else:
            result += c

    return result[::-1] if all(not c.isalpha() for c in s) else result

