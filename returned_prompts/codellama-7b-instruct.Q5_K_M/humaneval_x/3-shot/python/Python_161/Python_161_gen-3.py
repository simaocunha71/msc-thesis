    result = ''
    for c in s:
        if c.isalpha():
            result = result + c.lower() if c.isupper() else result + c.upper()
        else:
            result = result + c
    return result[::-1]


