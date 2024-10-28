def replace_spaces(string):
    new_str = ""
    for char in string:
        if char == " ":
            new_str += "_"
        else:
            new_str += char
    return new_str