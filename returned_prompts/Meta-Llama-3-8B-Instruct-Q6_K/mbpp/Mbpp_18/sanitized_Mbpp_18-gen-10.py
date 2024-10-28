def remove_dirty_chars(s1, s2):
    result = ""
    for char in s1:
        if char not in s2:
            result += char
    return result