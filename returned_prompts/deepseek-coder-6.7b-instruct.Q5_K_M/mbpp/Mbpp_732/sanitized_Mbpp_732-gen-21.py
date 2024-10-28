def replace_specialchar(string):
    special_char = [" ", ",", "."]
    for char in special_char:
        string = string.replace(char, ":")
    return string