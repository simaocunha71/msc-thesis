def remove_dirty_chars(string_1, string_2):
    return ''.join(char for char in string_1 if char not in string_2)