def remove_dirty_chars(string_1,string_2):
    return ''.join(ch for ch in string_1 if ch not in string_2)