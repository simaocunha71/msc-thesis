    result = ""
    for char in s:
        if char.isalpha():
            shift = 2 * (ord(char.lower()) - ord('a') + 2) % 26
            char = chr(ord('a') + shift)
            result += char if char.islower() else char.upper()
        else:
            result += char
    return result


