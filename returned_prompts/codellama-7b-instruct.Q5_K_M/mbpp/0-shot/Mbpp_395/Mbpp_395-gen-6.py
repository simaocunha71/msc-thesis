
# First, get all the characters in the string
# Next, get a list of all the characters in the string that are not the same as the previous character
# Finally, return the first item in the list, or None if the list is empty

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

# Test cases
assert first_non_repeating_character("abcabc") == None
assert first_non_repeating_character("abcdef") == 'e'
assert first_non_repeating_character("aabbcc") == None

# Improved solution
def first_non_repeating_character(string):
    for character in string:
        if string.count(character) == 1:
            return character
    return None

# Test cases
assert first_non_repeating_character("abcabc") == None
assert first_non_repeating_character("abcdef") == 'e'
assert first_non_repeating_character("aabbcc") == None
