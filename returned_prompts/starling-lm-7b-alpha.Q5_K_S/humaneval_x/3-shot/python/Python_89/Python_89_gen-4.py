    result = ""
    for letter in s:
        if letter == ' ':
            result += letter
        else:
            index = ord(letter)
            result += chr((index - 2 * 2) % 26 + 65)

    return result


