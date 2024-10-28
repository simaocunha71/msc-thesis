
def remove_dirty_chars(string1, string2):
    return ''.join(ch for ch in string1 if ch not in string2)


