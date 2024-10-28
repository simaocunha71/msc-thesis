    result = 0

    for char in s:
        if char.isupper():
            result += ord(char)

    return result


