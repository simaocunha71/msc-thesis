def remove_dirty_chars(string_1, string_2):
    clean_string = ''
    for char in string_1:
        if char not in string_2:
            clean_string += char
    return clean_string