    result = ""
    for char in s:
        if char.isalpha():
            shift = 6
            char_code = ord(char.lower())
            new_char_code = (char_code - 97 + shift) % 26 + 97
            result += chr(new_char_code) if char.islower() else chr(new_char_code).upper()
        else:
            result += char
    return result


