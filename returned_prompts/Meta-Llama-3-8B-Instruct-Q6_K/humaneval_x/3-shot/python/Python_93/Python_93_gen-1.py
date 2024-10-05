    result = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + 32) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) - 32) % 26 + 97)
        else:
            result += char
    return result


