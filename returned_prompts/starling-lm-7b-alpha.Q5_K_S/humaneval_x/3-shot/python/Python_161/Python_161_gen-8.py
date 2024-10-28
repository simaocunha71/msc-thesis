    result = ""
    for c in s:
        if c.isalpha():
            result += chr(ord(c) ^ 32) if c.islower() else chr(ord(c) - 32)
        else:
            result += c
    return result if result else s


