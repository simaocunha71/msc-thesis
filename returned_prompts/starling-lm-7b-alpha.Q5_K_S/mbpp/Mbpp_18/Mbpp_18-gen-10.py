
def remove_dirty_chars(string_1, string_2):
    for c in string_2:
        string_1 = string_1.replace(c, '')
    return string_1


