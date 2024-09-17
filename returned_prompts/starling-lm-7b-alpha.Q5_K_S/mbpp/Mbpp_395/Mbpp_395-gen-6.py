
def first_non_repeating_character(string):
    first_non_repeating_char = None
    for char in string:
        if string.count(char) == 1:
            first_non_repeating_char = char
            break
    return first_non_repeating_char


