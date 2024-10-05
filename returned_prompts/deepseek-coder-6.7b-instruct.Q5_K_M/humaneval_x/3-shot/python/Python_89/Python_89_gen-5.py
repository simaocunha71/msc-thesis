    result = ''
    for char in s:
        if 65 <= ord(char) <= 90:
            result += chr(((ord(char) - 65 + 2*2) % 26) + 65)
        elif 97 <= ord(char) <= 122:
            result += chr(((ord(char) - 97 + 2*2) % 26) + 97)
        else:
            result += char
    return result

