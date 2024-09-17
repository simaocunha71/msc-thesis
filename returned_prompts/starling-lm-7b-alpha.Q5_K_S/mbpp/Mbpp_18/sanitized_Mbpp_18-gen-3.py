def remove_dirty_chars(string1, string2):
    for i in string2:
        while i in string1:
            string1 = string1.replace(i, "")
    return string1