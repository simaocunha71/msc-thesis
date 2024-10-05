    result = ""
    for char in s:
        if 'A' <= char <= 'X':
            result += chr(ord(char) + 2)
        elif char == 'Y':
            result += 'A'
        elif char == 'Z':
            result += 'B'
        else:
            result += char
    return result

