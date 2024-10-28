    result = ""
    for letter in s:
        if letter.isalpha():
            ascii_offset = 65 if letter.isupper() else 97
            result += chr(((ord(letter) - ascii_offset + 2) % 26) + 2 * ascii_offset)
        else:
            result += letter
    return result


