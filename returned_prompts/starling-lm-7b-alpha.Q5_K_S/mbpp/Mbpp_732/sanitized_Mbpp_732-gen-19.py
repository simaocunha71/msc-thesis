def replace_specialchar(str):
    special_chars = [' ', ',', '.', ':']
    for char in special_chars:
        str = str.replace(char, ':')
    return str