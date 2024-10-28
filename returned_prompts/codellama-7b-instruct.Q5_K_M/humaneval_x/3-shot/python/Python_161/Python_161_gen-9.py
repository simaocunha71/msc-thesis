    result = ''
    for char in s:
        if char.isalpha():
            result += char.upper() if char.islower() else char.lower()
        else:
            result += char
    return result
