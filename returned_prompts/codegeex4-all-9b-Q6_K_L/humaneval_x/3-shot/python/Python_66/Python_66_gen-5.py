    total = 0
    for character in s:
        if character.isupper():
            total += ord(character)
    return total

