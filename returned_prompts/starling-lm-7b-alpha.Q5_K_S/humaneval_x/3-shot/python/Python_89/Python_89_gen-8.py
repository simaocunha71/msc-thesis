    result = ""
    for c in s:
        if c.isalpha():
            ascii_code = ord(c)
            if ascii_code >= 97:
                result += chr((ascii_code - 97 + 2 * 2) % 26 + 97)
            else:
                result += chr((ascii_code - 65 + 2 * 2) % 26 + 65)
        else:
            result += c
    return result


