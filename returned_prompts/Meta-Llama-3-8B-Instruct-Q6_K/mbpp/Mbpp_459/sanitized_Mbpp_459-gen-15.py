def remove_uppercase(s):
    result = ''
    uppercase_encountered = False
    for c in s:
        if c.isupper():
            uppercase_encountered = True
        elif uppercase_encountered:
            result += c.lower()
        else:
            result += c
    return result