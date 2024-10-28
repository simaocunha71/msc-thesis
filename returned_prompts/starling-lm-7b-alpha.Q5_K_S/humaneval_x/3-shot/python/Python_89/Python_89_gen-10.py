    result = []
    for letter in s:
        if letter == ' ':
            result.append(letter)
        else:
            ascii_val = ord(letter)
            new_ascii_val = ascii_val + 2 * 2
            result.append(chr(new_ascii_val))
    return "".join(result)


