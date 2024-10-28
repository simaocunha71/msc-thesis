
def replace_spaces(string):
    new_string = ""
    for char in string:
        if char == " ":
            new_string += "%20"
        else:
            new_string += char
    return new_string


