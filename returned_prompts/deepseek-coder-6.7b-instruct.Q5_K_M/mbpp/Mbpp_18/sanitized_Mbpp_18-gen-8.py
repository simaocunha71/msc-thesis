def remove_dirty_chars(str1, str2):
    for char in str2:
        str1 = str1.replace(char, '')
    return str1