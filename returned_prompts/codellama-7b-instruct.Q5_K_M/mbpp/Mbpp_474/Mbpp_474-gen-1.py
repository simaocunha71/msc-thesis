
def replace_char(my_string, char_to_replace, replacement_char):
    new_string = ''
    for char in my_string:
        if char == char_to_replace:
            new_string += replacement_char
        else:
            new_string += char
    return new_string


