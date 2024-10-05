
    result = ''

    for character in string:
        if character.islower():
            result += character.upper()
        else:
            result += character.lower()

    return result
