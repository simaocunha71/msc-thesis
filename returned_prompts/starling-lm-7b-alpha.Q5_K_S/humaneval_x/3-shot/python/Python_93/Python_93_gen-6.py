    vowels = "AEIOU"
    result = ""
    for c in message:
        if c.isalpha():
            if c.upper() in vowels:
                result += chr((ord(c.upper()) + 2) % 26 + ord('A'))
            else:
                result += chr((ord(c) + 2) % 26 + ord('a'))
        else:
            result += c
    return result


