def first_non_repeating_character(string):
    # Get all the characters in the string
    # [a, b, c]
    characters = list(string)

    # Get a list of all the characters in the string that are not the same as the previous character
    # ['a', 'b', 'c']
    first_characters = []
    for character in characters:
        if character != characters[0]:
            first_characters.append(character)

    # Finally, return the first item in the list, or None if the list is empty
    if first_characters:
        return first_characters[0]
    else:
        return None