def remove_dirty_chars(string1, string2):
    for char in string2:
        if char in string1:
            string1 = string1.replace(char, "")
    return string1