    result = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in s:
        if letter in alphabet:
            index = alphabet.index(letter)
            index += 2 * 2
            if index >= 26:
                index -= 26
            result += alphabet[index]
        else:
            result += letter
    return result

