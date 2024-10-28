def first_non_repeating_character(s):
    character_frequency = {}

    # Get the frequency of each character in the string
    for char in s:
        if char in character_frequency:
            character_frequency[char] += 1
        else:
            character_frequency[char] = 1

    # Check the string again to find the first non-repeating character
    for char in s:
        if character_frequency[char] == 1:
            return char

    return None