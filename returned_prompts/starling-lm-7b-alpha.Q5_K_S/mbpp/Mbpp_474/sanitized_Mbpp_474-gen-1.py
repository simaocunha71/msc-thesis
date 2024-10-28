def replace_char(string, char1, char2):
    new_string = ""
    for c in string:
        if c == char1:
            new_string += char2
        else:
            new_string += c
    return new_string